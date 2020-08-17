import collections

import pytest

from AutomationFramework.utils.rpc_automator_2 import RPCAutomator2
from AutomationFramework.capabilities import HOSTS
import xmltodict


class BasePageObject:
    rpc_automator = None
    test_case_file = None
    test_case_name = None
    test_case = None
    netconf_filter = None
    get_config_response = None
    edit_config_first_get_config_response = None
    edit_config_second_get_config_response = None
    rendered_template = None
    variables_to_commit = {}
    values_before_commit = {}
    values_after_commit = {}
    state_values_after_get = {}
    values_where_changed_after_test = False
    get_response = None
    values_after_get = {}

    def __init__(self, test_case_file=None, test_case_name=None, rpc_idx=0):
        self.rpc_automator = RPCAutomator2(HOSTS[0])
        self.test_case_file = test_case_file
        self.test_case_name = test_case_name
        self.test_case = self.rpc_automator.get_test_case_by_name_from_file(file=self.test_case_file,
                                                                            test_case_name=self.test_case_name)
        self.set_variables_to_commit(rpc_idx)

    def set_variables_to_commit(self, rpc_idx):
        self.variables_to_commit = dict(self.test_case['testcase']['rpcs'][rpc_idx]['params'])

    def execute_edit_config_test_case(self):
        if self.netconf_filter:
            pass
        else:
            self.generate_filter_from_test_case()
        self.execute_edit_config_first_get_config_with_filter()
        self.get_rendered_template()
        self.execute_edit_config_with_template()
        self.execute_edit_config_second_get_config_with_filter()

    def set_filter(self, new_filter):
        self.netconf_filter = new_filter

    #TODO: ¿? implement generate_filter_from_test_case() in rpc_automator
    def generate_filter_from_test_case(self):
        # self.netconf_filter = self.rpc_automator.generate_filter_from_test_case()
        self.netconf_filter = """
                    <filter>
                    </filter>
                    """

    def execute_get_config_with_filter(self):
        self.get_config_response = self.rpc_automator.safe_get_config(netconf_filter=self.netconf_filter,
                                                                      test_case=self.test_case)
        return self.get_config_response

    def get_rendered_template(self):
        print('---------------------------------------------------------------------------------------')
        print('Rendered template')
        self.rendered_template = self.rpc_automator.rpc_body_generator(test_case=self.test_case, rpc_index=0)
        print(self.rendered_template)
        return self.rendered_template

    def execute_edit_config_with_template(self, template=None):
        if template:
            self.rpc_automator.safe_dispatch(template=template)
        else:
            self.rpc_automator.safe_dispatch(template=self.rendered_template)

    def execute_edit_config_first_get_config_with_filter(self):
        print('---------------------------------------------------------------------------------------')
        print('First get_config response')
        self.edit_config_first_get_config_response = self.rpc_automator.safe_get_config(
            netconf_filter=self.netconf_filter, test_case=self.test_case)
        print(self.edit_config_first_get_config_response)
        return self.edit_config_first_get_config_response

    def execute_edit_config_second_get_config_with_filter(self):
        print('---------------------------------------------------------------------------------------')
        print('Second get_config response')
        self.edit_config_second_get_config_response = self.rpc_automator.safe_get_config(
            netconf_filter=self.netconf_filter, test_case=self.test_case)
        print(self.edit_config_second_get_config_response)
        return self.edit_config_second_get_config_response

    def get_variable_value_for_rpc_in_test_case(self, variable, rpc_index=0):
        return self.test_case['testcase']['rpcs'][rpc_index]['params'][variable]

    def validate_test_case_params(self):
        print('---------------------------------------------------------------------------------------')
        print('Validation')
        print('- Values before edit-config')
        print(self.values_before_commit)
        print('- Values after edit-config')
        print(self.values_after_commit)
        print('- Values to validate')
        print(self.variables_to_commit)
        self.verify_test_and_skip()
        test_passes = True
        for key, value in self.variables_to_commit.items():
            if isinstance(self.values_after_commit[key], collections.abc.Mapping):
                if value not in self.values_after_commit[key]['#text']:
                    test_passes = False
            else:
                if self.values_after_commit[key] != value:
                    test_passes = False
        return test_passes

    def validate_get_test_case(self):
        print('---------------------------------------------------------------------------------------')
        print('Validation')
        print('- Values after get')
        print(self.values_after_get)
        test_passes = True
        for key, value in self.values_after_get.items():
            if not self.values_after_get[key]:
                test_passes = False
        return test_passes

    def get_test_case_description(self):
        return self.test_case['testcase']['description']

    def verify_test_and_skip(self):
        self.values_where_changed_after_test = True
        skip_test = True
        for key, value in self.variables_to_commit.items():
            if isinstance(self.values_before_commit[key], collections.abc.Mapping):
                if value not in self.values_before_commit[key]['#text']:
                    skip_test = False
            else:
                if self.values_before_commit[key] != value:
                    skip_test = False
        if skip_test:
            self.values_where_changed_after_test = False
            pytest.skip('The actual value of the params tested is the same of the test´s expected value. '
                        'For performing the test change either the actual value or the test´s expected value')

    def get_rpc_reply_key_from_get_config(self):
        if self.get_config_response:
            response_dict = xmltodict.parse(self.get_config_response.xml)
        else:
            if self.edit_config_first_get_config_response:
                response_dict = xmltodict.parse(self.edit_config_first_get_config_response.xml)
            else:
                return None
        for keys in response_dict:
            if 'rpc-reply' in keys:
                return keys
        return None

    def get_data_key_from_get_config(self, rpc_reply_key):
        if self.get_config_response:
            response_dict = xmltodict.parse(self.get_config_response.xml)[rpc_reply_key]
        else:
            if self.edit_config_first_get_config_response:
                response_dict = xmltodict.parse(self.edit_config_first_get_config_response.xml)[rpc_reply_key]
            else:
                return None
        for keys in response_dict:
            if 'data' in keys:
                return keys
        return None

    def clean_after_test(self):
        print('---------------------------------------------------------------------------------------')
        print('Cleaning up')
        initial_values = self.get_initial_values_of_params_changed()
        # Conditional statement to see if the data needs to be deleted or wrote back
        initial_values_template = self.rpc_automator.rpc_body_generator(test_case=self.test_case, rpc_index=0,
                                                                        variables_in_template=initial_values)
        print('- Template with initial values')
        print(initial_values_template)
        self.execute_edit_config_with_template(template=initial_values_template)
        print('- Get-config after cleaning')
        print(self.rpc_automator.safe_get_config(netconf_filter=self.netconf_filter, test_case=self.test_case))

    def get_initial_values_of_params_changed(self):
        initial_values = {}
        for key in self.variables_to_commit:
            if isinstance(self.values_before_commit[key], collections.abc.Mapping):
                initial_values[key] = self.values_before_commit[key]['#text'].split(':')[-1]
            else:
                initial_values[key] = self.values_before_commit[key]
        return initial_values

    def execute_get_test_case(self):
        self.get_rendered_template()
        self.execute_get_with_template()
        self.set_values_after_get()

    def set_values_after_get(self):
        rpc_reply_key = self.get_rpc_reply_key_from_get_response()
        data_key = self.get_data_key_from_get_response(rpc_reply_key=rpc_reply_key)
        parsed_dict = xmltodict.parse(self.get_response.xml)[rpc_reply_key][data_key]
        keys_to_set = []
        for key, item in self.variables_to_commit.items():
            if not item:
                if '_' in key:
                    keys_to_set.append(key.replace('_', '-'))
                else:
                    keys_to_set.append(key)

        for key_to_search in keys_to_set:
            self.values_after_get[key_to_search] = self.get_tag_value_in_given_dict(tag_value=key_to_search,
                                                                                    parsed_dict=parsed_dict)

    def get_tag_value_in_given_dict(self, tag_value, parsed_dict):
        recursive_return = None
        for key, item in parsed_dict.items():
            if key == tag_value:
                return parsed_dict[key]
            else:
                if isinstance(parsed_dict[key], collections.abc.Mapping):
                    recursive_return = self.get_tag_value_in_given_dict(tag_value=tag_value,
                                                                        parsed_dict=parsed_dict[key])
            if recursive_return:
                break
        return recursive_return

    def get_rpc_reply_key_from_get_response(self):
        response_dict = xmltodict.parse(self.get_response.xml)
        for keys in response_dict:
            if 'rpc-reply' in keys:
                return keys
        return None

    def get_data_key_from_get_response(self, rpc_reply_key):
        response_dict = xmltodict.parse(self.get_response.xml)[rpc_reply_key]
        for keys in response_dict:
            if 'data' in keys:
                return keys
        return None

    def execute_get_with_template(self, template=None):
        if template:
            self.get_response = self.rpc_automator.safe_get(template=template)
        else:
            self.get_response = self.rpc_automator.safe_get(template=self.rendered_template)
        print('---------------------------------------------------------------------------------------')
        print('- get response')
        print(self.get_response)
        return self.get_response

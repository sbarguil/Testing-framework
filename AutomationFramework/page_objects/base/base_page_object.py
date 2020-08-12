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

    def execute_edit_config_with_template(self):
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
                if self.values_after_commit[key]['#text'] != value:
                    test_passes = False
            else:
                if self.values_after_commit[key] != value:
                    test_passes = False
        return test_passes

    def get_test_case_description(self):
        return self.test_case['testcase']['description']

    # TODO
    def verify_test_and_skip(self):
        # pytest.skip('') if the initial values are the same as the expected values
        pass

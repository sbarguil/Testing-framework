import os
from pathlib import Path
import xmltodict
from ncclient import manager
import yaml
from lxml import etree as et
from jinja2 import Environment, PackageLoader, select_autoescape
from collections import OrderedDict


class RPCAutomator2:
    def __init__(self, connection):
        self.host = connection['host']
        self.port = connection['port']
        self.username = connection['username']
        self.password = connection['password']
        self.manager = None
        self.set_connection()
        self.jinja_env = Environment(
            loader=PackageLoader('AutomationFramework', 'test_cases/templates'),
            autoescape=select_autoescape(['xml'])
        )

    def set_connection(self):
        self.manager = manager.connect(host=self.host,
                                       port=self.port,
                                       username=self.username,
                                       password=self.password,
                                       hostkey_verify=False,
                                       look_for_keys=False,
                                       allow_agent=False,
                                       device_params={'name': 'huawei'},
                                       )

    def rpc_body_generator(self, test_case, rpc_index=0, variables_in_template=None):
        template_file_name = test_case['testcase']['rpcs'][rpc_index]['template']
        jinja_template = self.jinja_env.get_template(template_file_name)
        rpc_list = test_case['testcase']['rpcs']
        if variables_in_template:
            jinja_variables_dict = variables_in_template
        else:
            jinja_variables_dict = rpc_list[rpc_index]['params']

        if 'target' in rpc_list[rpc_index]:
            jinja_variables_dict['target'] = rpc_list[rpc_index]['target']

        return jinja_template.render(jinja_variables_dict)

    def get_occurrences_of_variable_in_not_rendered_template(self, test_case, rpc_index, variable_in_test_case):
        template_file_name = test_case['testcase']['rpcs'][rpc_index]['template']
        not_windows_path = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
        template_file_path = Path(not_windows_path.replace('/utils', '')) / 'test_cases/templates' / template_file_name
        file = open(template_file_path, 'r')
        data = file.read()
        text_to_search = '{{' + variable_in_test_case + '}}'
        occurrences = data.count(text_to_search)
        return occurrences

    def generate_filter_from_test_case(self, test_case, rpc_index=0):
        template_file_name = test_case['testcase']['rpcs'][rpc_index]['template']
        jinja_template = self.jinja_env.get_template(template_file_name)

        rpc_list = test_case['testcase']['rpcs']
        jinja_variables_dict = rpc_list[rpc_index]['params']
        jinja_variables_dict['target'] = rpc_list[rpc_index]['target']
        if 'target' in rpc_list[rpc_index]:
            jinja_variables_dict['target'] = rpc_list[rpc_index]['target']

        filled_template = jinja_template.render(jinja_variables_dict)
        parsed_dict = xmltodict.parse(filled_template)
        full_filter_dict = OrderedDict()
        full_filter_dict['filter'] = parsed_dict['edit-config']['config']
        full_filter = xmltodict.unparse(full_filter_dict)
        return full_filter

    def get_rpc_target_from_test_case(self, test_case, rpc_index=0):
        rpc_list = test_case['testcase']['rpcs']
        return rpc_list[rpc_index]['target']

    def safe_dispatch(self, template):
        try:
            full_response = '- Response of edit-config: '
            print('- Response of edit-config')
            response_edit_config = str(self.manager.dispatch(et.fromstring(template)))
            print(response_edit_config)
            full_response = full_response + response_edit_config + ' \n\n - Response of commit: '
            print('- Response of commit')
            response_commit = str(self.manager.dispatch(et.fromstring("<commit/>")))
            print(response_commit)
            full_response = full_response + response_commit
            return full_response
        except Exception as e:
            print("An exception has occurred when performing the edit_config operation.")
            raise e

    def safe_discard_changes(self):
        try:
            full_response = '- Response of discard-changes: '
            print(full_response)
            response_discard_changes = str(self.manager.dispatch(et.fromstring("<discard-changes/>")))
            print(response_discard_changes)
            full_response = full_response + response_discard_changes
            return full_response
        except Exception as e:
            print("An exception has occurred when performing the discard-changes operation.")
            raise e

    def safe_dispatch_no_commit(self, template):
        try:
            print('- Response of dispatch without commit')
            response = self.manager.dispatch(et.fromstring(template))
            print(response)
            return response
        except Exception as e:
            print("An exception has occurred when performing the edit_config operation.")
            raise e

    def safe_get(self, template):
        try:
            return self.manager.get(("subtree", template))
        except Exception as e:
            print("An exception has occurred when performing the get operation.")
            raise e

    def safe_get_config(self, netconf_filter, test_case, rpc_index=0):
        target = self.get_rpc_target_from_test_case(test_case=test_case, rpc_index=rpc_index)
        try:
            return self.manager.get_config(source=target, filter=netconf_filter)
        except Exception as e:
            print("An exception has occurred when performing the get_config operation.")
            raise e

    def get_test_case_by_name_from_file(self, file, test_case_name):
        loaded_file = None
        specified_test_case = None
        with open("test_cases/{}".format(file), 'r') as stream:
            try:
                loaded_file = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        idx = 0
        while idx < len(loaded_file) and not specified_test_case:
            if loaded_file[idx]['testcase']['name'] == test_case_name:
                specified_test_case = loaded_file[idx]
            idx = idx + 1
        print("**********************************************************",specified_test_case)
        return specified_test_case

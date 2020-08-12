from ncclient import manager
import yaml
from lxml import etree as et
from jinja2 import Environment, PackageLoader, select_autoescape


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
                                       allow_agent=False
                                       )

    def rpc_body_generator(self, test_case, rpc_index=0):
        template_file_name = test_case['testcase']['rpcs'][rpc_index]['template']
        jinja_template = self.jinja_env.get_template(template_file_name)
        rpc_list = test_case['testcase']['rpcs']
        jinja_variables_dict = rpc_list[rpc_index]['params']
        jinja_variables_dict['target'] = rpc_list[rpc_index]['target']

        return jinja_template.render(jinja_variables_dict)

    # TODO
    def generate_filter_from_test_case(self):
        pass

    def get_rpc_target_from_test_case(self, test_case, rpc_index=0):
        rpc_list = test_case['testcase']['rpcs']
        return rpc_list[rpc_index]['target']

    def safe_dispatch(self, template):
        try:
            self.manager.dispatch(et.fromstring(template))
            self.manager.dispatch(et.fromstring("<commit/>"))
        except Exception as e:
            print("An exception has occurred when performing the edit_config operation.")
            raise e

    def safe_get_config(self, netconf_filter, test_case):
        target = self.get_rpc_target_from_test_case(test_case=test_case, rpc_index=0)
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

        return specified_test_case

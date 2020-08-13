import xmltodict
from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class Interfaces(BasePageObject):
    values_before_commit = {
        'name': None,
        'type': None,
        'enabled': None,
        'description': None,
        'mtu': None,
        'loopback-mode': None,
        'tpid': None,
    }
    values_after_commit = {
        'name': None,
        'type': None,
        'enabled': None,
        'description': None,
        'mtu': None,
        'loopback-mode': None,
        'tpid': None,
    }

    def execute_interfaces_edit_config_test_case(self):
        filter_to_use = """
                    <filter>
                        <interfaces xmlns="http://openconfig.net/yang/interfaces">
                        <interface>
                        <name>{}</name>
                        </interface>
                        </interfaces>
                    </filter>
                    """
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=0, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_edit_config_test_case()
        self.set_values_before_commit_dict()
        self.set_values_after_commit_dict()

    def set_values_before_commit_dict(self):
        rpc_reply_key = self.get_rpc_reply_key_from_get_config()
        data_key = self.get_data_key_from_get_config(rpc_reply_key=rpc_reply_key)
        parsed_dict = xmltodict.parse(
            self.edit_config_first_get_config_response.xml)[rpc_reply_key][data_key]['interfaces']['interface']['config']
        if 'name' in parsed_dict:
            self.values_before_commit['name'] = parsed_dict['name']
        if 'type' in parsed_dict:
            self.values_before_commit['type'] = parsed_dict['type']
        if 'enabled' in parsed_dict:
            self.values_before_commit['enabled'] = parsed_dict['enabled']
        if 'description' in parsed_dict:
            self.values_before_commit['description'] = parsed_dict['description']
        if 'mtu' in parsed_dict:
            self.values_before_commit['mtu'] = parsed_dict['mtu']
        if 'loopback-mode' in parsed_dict:
            self.values_before_commit['loopback-mode'] = parsed_dict['loopback-mode']
        if 'tpid' in parsed_dict:
            self.values_before_commit['tpid'] = parsed_dict['tpid']

    def set_values_after_commit_dict(self):
        rpc_reply_key = self.get_rpc_reply_key_from_get_config()
        data_key = self.get_data_key_from_get_config(rpc_reply_key=rpc_reply_key)
        parsed_dict = xmltodict.parse(
            self.edit_config_second_get_config_response.xml)[rpc_reply_key][data_key]['interfaces']['interface']['config']
        if 'name' in parsed_dict:
            self.values_after_commit['name'] = parsed_dict['name']
        if 'type' in parsed_dict:
            self.values_after_commit['type'] = parsed_dict['type']
        if 'enabled' in parsed_dict:
            self.values_after_commit['enabled'] = parsed_dict['enabled']
        if 'description' in parsed_dict:
            self.values_after_commit['description'] = parsed_dict['description']
        if 'mtu' in parsed_dict:
            self.values_after_commit['mtu'] = parsed_dict['mtu']
        if 'loopback-mode' in parsed_dict:
            self.values_after_commit['loopback-mode'] = parsed_dict['loopback-mode']
        if 'tpid' in parsed_dict:
            self.values_after_commit['tpid'] = parsed_dict['tpid']

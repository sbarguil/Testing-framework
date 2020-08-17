import xmltodict
from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class Interfaces(BasePageObject):
    values_before_commit = {
        'name': None,
        'type': None,
        'enabled': None,
        'description': None,
        'mtu': None,
        'loopback_mode': None,
        'tpid': None,
        'auto_negotiate': None,
        'duplex_mode': None,
        'port_speed': None,
        'aggregate_id': None,
    }
    values_after_commit = {
        'name': None,
        'type': None,
        'enabled': None,
        'description': None,
        'mtu': None,
        'loopback_mode': None,
        'tpid': None,
        'auto_negotiate': None,
        'duplex_mode': None,
        'port_speed': None,
        'aggregate_id': None,
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
            self.edit_config_first_get_config_response.xml)[rpc_reply_key][data_key]['interfaces']['interface']

        if 'config' in parsed_dict:
            if 'name' in parsed_dict['config']:
                self.values_before_commit['name'] = parsed_dict['config']['name']
            if 'type' in parsed_dict['config']:
                self.values_before_commit['type'] = parsed_dict['config']['type']
            if 'enabled' in parsed_dict['config']:
                self.values_before_commit['enabled'] = parsed_dict['config']['enabled']
            if 'description' in parsed_dict['config']:
                self.values_before_commit['description'] = parsed_dict['config']['description']
            if 'mtu' in parsed_dict['config']:
                self.values_before_commit['mtu'] = parsed_dict['config']['mtu']
            if 'loopback-mode' in parsed_dict['config']:
                self.values_before_commit['loopback_mode'] = parsed_dict['config']['loopback-mode']
            if 'tpid' in parsed_dict['config']:
                self.values_before_commit['tpid'] = parsed_dict['config']['tpid']

            if 'ethernet' in parsed_dict['config']:
                if 'auto-negotiate' in parsed_dict['ethernet']['config']:
                    self.values_before_commit['auto_negotiate'] = parsed_dict['ethernet']['config']['auto-negotiate']
                if 'duplex-mode' in parsed_dict['ethernet']['config']:
                    self.values_before_commit['duplex_mode'] = parsed_dict['ethernet']['config']['duplex-mode']
                if 'port-speed' in parsed_dict['ethernet']['config']:
                    self.values_before_commit['port_speed'] = parsed_dict['ethernet']['config']['port-speed']
                if 'aggregate-id' in parsed_dict['ethernet']['config']:
                    self.values_before_commit['aggregate_id'] = parsed_dict['ethernet']['config']['aggregate-id']

    def set_values_after_commit_dict(self):
        rpc_reply_key = self.get_rpc_reply_key_from_get_config()
        data_key = self.get_data_key_from_get_config(rpc_reply_key=rpc_reply_key)
        parsed_dict = xmltodict.parse(
            self.edit_config_second_get_config_response.xml)[rpc_reply_key][data_key]['interfaces']['interface']
        if 'config' in parsed_dict:
            if 'name' in parsed_dict['config']:
                self.values_after_commit['name'] = parsed_dict['config']['name']
            if 'type' in parsed_dict['config']:
                self.values_after_commit['type'] = parsed_dict['config']['type']
            if 'enabled' in parsed_dict['config']:
                self.values_after_commit['enabled'] = parsed_dict['config']['enabled']
            if 'description' in parsed_dict['config']:
                self.values_after_commit['description'] = parsed_dict['config']['description']
            if 'mtu' in parsed_dict['config']:
                self.values_after_commit['mtu'] = parsed_dict['config']['mtu']
            if 'loopback-mode' in parsed_dict['config']:
                self.values_after_commit['loopback_mode'] = parsed_dict['config']['loopback-mode']
            if 'tpid' in parsed_dict['config']:
                self.values_after_commit['tpid'] = parsed_dict['config']['tpid']

            if 'ethernet' in parsed_dict['config']:
                if 'auto-negotiate' in parsed_dict['ethernet']['config']:
                    self.values_after_commit['auto_negotiate'] = parsed_dict['ethernet']['config']['auto-negotiate']
                if 'duplex-mode' in parsed_dict['ethernet']['config']:
                    self.values_after_commit['duplex_mode'] = parsed_dict['ethernet']['config']['duplex-mode']
                if 'port-speed' in parsed_dict['ethernet']['config']:
                    self.values_after_commit['port_speed'] = parsed_dict['ethernet']['config']['port-speed']
                if 'aggregate-id' in parsed_dict['ethernet']['config']:
                    self.values_after_commit['aggregate_id'] = parsed_dict['ethernet']['config']['aggregate-id']

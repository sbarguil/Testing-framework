import xmltodict
from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class Interfaces(BasePageObject):
    variables_paths = {
        'if_subif_type': [
            {
                'name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type'
            }
        ],
        'if_subif_description': [
            {
                'name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'description': 'interfaces/interface/subinterfaces/subinterface/config/description',
            }
        ],
        'if_subif_enabled': [
            {
                'name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'enabled': 'interfaces/interface/subinterfaces/subinterface/config/enabled',
            }
        ],
        'if_subif_ip_prefix_length': [
            {
                'name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'ip': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/ip',
                'prefix_length': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/config/prefix-length',
            }
        ],
        'if_subif_dhcp_client': [
            {
                'name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'dhcp_client': 'interfaces/interface/subinterfaces/subinterface/ipv4/config/dhcp-client',
            }
        ],
        'if_subif_mtu': [
            {
                'name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'mtu': 'interfaces/interface/subinterfaces/subinterface/ipv4/config/mtu',
            }
        ],
        'if_subif_vlan_id': [
            {
                'name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'vlan_id': 'interfaces/interface/subinterfaces/subinterface/vlan/config/vlan-id',
            }
        ],
        'if_subif_inner_outer_vlan_id': [
            {
                'name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'inner_vlan_id': 'interfaces/interface/subinterfaces/subinterface/vlan/match/double-tagged/config/inner-vlan-id',
                'outer_vlan_id': 'interfaces/interface/subinterfaces/subinterface/vlan/match/double-tagged/config/outer-vlan-id',
            }
        ],
        'if_subif_match_vlan_id': [
            {
                'name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'vlan_id': 'interfaces/interface/subinterfaces/subinterface/vlan/match/single-tagged/config/vlan-id',
            }
        ],
    }

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

    def execute_generic_interfaces_edit_config_test_case(self):
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
        self.execute_generic_edit_config_test_case()

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

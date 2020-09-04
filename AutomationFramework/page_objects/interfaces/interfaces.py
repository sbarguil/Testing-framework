import xmltodict
from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class Interfaces(BasePageObject):
    variables_paths = {
        'if_subif_type': [
            {
                'interface_name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type'
            }
        ],
        'if_subif_description': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'description': 'interfaces/interface/subinterfaces/subinterface/config/description',
            }
        ],
        'if_subif_enabled': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'enabled': 'interfaces/interface/subinterfaces/subinterface/config/enabled',
            }
        ],
        'if_subif_ip_prefix_length': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'ip': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/ip',
                'prefix_length': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/config/prefix-length',
            }
        ],
        'if_subif_ip_state': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'ip': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/ip',
                'prefix_length': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/config/prefix-length',
            },
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'ip': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/state/ip',
            }
        ],
        'if_subif_origin': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'ip': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/ip',
                'prefix_length': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/config/prefix-length',
            },
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'origin': 'interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/state/origin',
            }
        ],
        'if_subif_dhcp_client': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'dhcp_client': 'interfaces/interface/subinterfaces/subinterface/ipv4/config/dhcp-client',
            }
        ],
        'if_subif_mtu': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'mtu': 'interfaces/interface/subinterfaces/subinterface/ipv4/config/mtu',
            }
        ],
        'if_subif_vlan_id': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'vlan_id': 'interfaces/interface/subinterfaces/subinterface/vlan/config/vlan-id',
            }
        ],
        'if_subif_inner_outer_vlan_id': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'inner_vlan_id': 'interfaces/interface/subinterfaces/subinterface/vlan/match/double-tagged/config/inner-vlan-id',
                'outer_vlan_id': 'interfaces/interface/subinterfaces/subinterface/vlan/match/double-tagged/config/outer-vlan-id',
            }
        ],
        'if_subif_match_vlan_id': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
                'vlan_id': 'interfaces/interface/subinterfaces/subinterface/vlan/match/single-tagged/config/vlan-id',
            }
        ],
        'if_status_admin_status': [
            {
                'interface_name': 'interfaces/interface/name',
                'admin_status': 'interfaces/interface/state/admin-status',
            }
        ],
        'if_status_enabled': [
            {
                'interface_name': 'interfaces/interface/name',
                'enabled': 'interfaces/interface/state/enabled',
            }
        ],
        'if_status_name': [
            {
                'interface_name': 'interfaces/interface/name',
                'empty_name': 'interfaces/interface/state/name',
            }
        ],
        'if_status_oper_status': [
            {
                'interface_name': 'interfaces/interface/name',
                'oper_status': 'interfaces/interface/state/oper-status',
            }
        ],
        'if_lag_type': [
            {
                'name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type',
                'enabled': 'interfaces/interface/config/enabled',
                'lag_type': 'interfaces/interface/aggregation/config/lag-type',
            }
        ],
        'if_lag_min_links': [
            {
                'name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type',
                'enabled': 'interfaces/interface/config/enabled',
                'min_links': 'interfaces/interface/aggregation/config/min-links',
            }
        ],
        'if_ethernet_auto_negotiate': [
            {
                'interface_name': 'interfaces/interface/name',
                'auto_negotiate': 'interfaces/interface/ethernet/config/auto-negotiate',
            }
        ],
        'if_ethernet_port_speed': [
            {
                'interface_name': 'interfaces/interface/name',
                'port_speed': 'interfaces/interface/ethernet/config/port-speed',
            }
        ],
        'if_ethernet_duplex_mode': [
            {
                'interface_name': 'interfaces/interface/name',
                'duplex_mode': 'interfaces/interface/ethernet/config/duplex-mode',
            }
        ],
        'if_ethernet_port_speed_state': [
            {
                'interface_name': 'interfaces/interface/name',
                'port_speed': 'interfaces/interface/ethernet/state/port-speed',
            }
        ],
        'if_ethernet_aggregate_id': [
            {
                'interface_name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type',
                'enabled': 'interfaces/interface/config/enabled',
            },
            {
                'interface_name': 'interfaces/interface/name',
                'aggregate_id': 'interfaces/interface/ethernet/config/aggregate-id',
            }
        ],
        'if_gre_dst': [
            {
                'interface_name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type',
                'dst': 'interfaces/interface/tunnel/config/dst',
            }
        ],
        'if_gre_src': [
            {
                'interface_name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type',
                'src': 'interfaces/interface/tunnel/config/src',
            }
        ],
        'if_gre_ttl': [
            {
                'interface_name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type',
                'ttl': 'interfaces/interface/tunnel/config/ttl',
            }
        ],
        'if_gre_ip_prefix_length': [
            {
                'interface_name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type',
                'ip': 'interfaces/interface/tunnel/ipv4/addresses/address/ip',
                'prefix_length': 'interfaces/interface/tunnel/ipv4/addresses/address/config/prefix-length',
            }
        ],
        'if_gre_mtu': [
            {
                'interface_name': 'interfaces/interface/name',
                'type': 'interfaces/interface/config/type',
                'mtu': 'interfaces/interface/tunnel/ipv4/config/mtu',
            }
        ],
    }

    values_before_commit = {
        'interface_name': None,
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
        'aggregation:config:lag_type': None,
        'aggregation:config:min_links': None,
    }
    values_after_commit = {
        'interface_name': None,
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
        'aggregation:config:lag_type': None,
        'aggregation:config:min_links': None,
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
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=0, variable='interface_name')
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
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=self.rpc_idx_in_test_case,
                                                                      variable='interface_name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()

    def execute_interface_rpc(self):
        if self.rpcs_list[self.rpc_idx_in_test_case]['operation'] == 'edit-config':
            self.execute_generic_interfaces_edit_config_test_case()
        elif self.rpcs_list[self.rpc_idx_in_test_case]['operation'] == 'get':
            self.execute_get_test_case_with_dispatch()

    def set_values_before_commit_dict(self):
        rpc_reply_key = self.get_rpc_reply_key_from_get_config()
        data_key = self.get_data_key_from_get_config(rpc_reply_key=rpc_reply_key)
        parsed_dict = xmltodict.parse(
            self.edit_config_first_get_config_response.xml)[rpc_reply_key][data_key]['interfaces']['interface']

        if 'config' in parsed_dict:
            if 'name' in parsed_dict['config']:
                self.values_before_commit['interface_name'] = parsed_dict['config']['name']
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

        if 'ethernet' in parsed_dict:
            if 'auto-negotiate' in parsed_dict['ethernet']['config']:
                self.values_before_commit['auto_negotiate'] = parsed_dict['ethernet']['config']['auto-negotiate']
            if 'duplex-mode' in parsed_dict['ethernet']['config']:
                self.values_before_commit['duplex_mode'] = parsed_dict['ethernet']['config']['duplex-mode']
            if 'port-speed' in parsed_dict['ethernet']['config']:
                self.values_before_commit['port_speed'] = parsed_dict['ethernet']['config']['port-speed']
            if 'aggregate-id' in parsed_dict['ethernet']['config']:
                self.values_before_commit['aggregate_id'] = parsed_dict['ethernet']['config']['aggregate-id']

        if 'aggregation' in parsed_dict:
            if 'lag-type' in parsed_dict['aggregation']['config']:
                self.values_before_commit['aggregation:config:lag_type'] = parsed_dict['aggregation']['config']['lag-type']
            if 'min-links' in parsed_dict['aggregation']['config']:
                self.values_before_commit['aggregation:config:min_links'] = parsed_dict['aggregation']['config']['min-links']

    def set_values_after_commit_dict(self):
        rpc_reply_key = self.get_rpc_reply_key_from_get_config()
        data_key = self.get_data_key_from_get_config(rpc_reply_key=rpc_reply_key)
        parsed_dict = xmltodict.parse(
            self.edit_config_second_get_config_response.xml)[rpc_reply_key][data_key]['interfaces']['interface']
        if 'config' in parsed_dict:
            if 'name' in parsed_dict['config']:
                self.values_after_commit['interface_name'] = parsed_dict['config']['name']
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

        if 'ethernet' in parsed_dict:
            if 'auto-negotiate' in parsed_dict['ethernet']['config']:
                self.values_after_commit['auto_negotiate'] = parsed_dict['ethernet']['config']['auto-negotiate']
            if 'duplex-mode' in parsed_dict['ethernet']['config']:
                self.values_after_commit['duplex_mode'] = parsed_dict['ethernet']['config']['duplex-mode']
            if 'port-speed' in parsed_dict['ethernet']['config']:
                self.values_after_commit['port_speed'] = parsed_dict['ethernet']['config']['port-speed']
            if 'aggregate-id' in parsed_dict['ethernet']['config']:
                self.values_after_commit['aggregate_id'] = parsed_dict['ethernet']['config']['aggregate-id']

        if 'aggregation' in parsed_dict:
            if 'lag-type' in parsed_dict['aggregation']['config']:
                self.values_after_commit['aggregation:config:lag_type'] = parsed_dict['aggregation']['config']['lag-type']
            if 'min-links' in parsed_dict['aggregation']['config']:
                self.values_after_commit['aggregation:config:min_links'] = parsed_dict['aggregation']['config']['min-links']

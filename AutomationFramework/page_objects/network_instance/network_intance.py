from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class NetworkInstance(BasePageObject):
    variables_paths = {
        'ni_config_name': [
            {
                'name': 'network-instances/network-instance/name',
            }
        ],
        'ni_get_name': [
            {
                'name': 'network-instances/network-instance/name',
            }
        ],
        'ni_config_type': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type'
            }
        ],
        'ni_config_enabled': [
            {
                'name': 'network-instances/network-instance/name',
                'enabled': 'network-instances/network-instance/config/enabled'
            }
        ],
        'ni_config_description': [
            {
                'name': 'network-instances/network-instance/name',
                'description': 'network-instances/network-instance/config/description'
            }
        ],
        'ni_config_router_id': [
            {
                'name': 'network-instances/network-instance/name',
                'router_id': 'network-instances/network-instance/config/router-id'
            }
        ],
        'ni_config_route_distinguisher': [
            {
                'name': 'network-instances/network-instance/name',
                'route_distinguisher': 'network-instances/network-instance/config/route-distinguisher'
            }
        ],
        'ni_config_enabled_address_families': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'enabled_address_families': 'network-instances/network-instance/config/enabled-address-families'
            }
        ],
        'ni_config_mtu': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'mtu': 'network-instances/network-instance/config/mtu',
            }
        ],
        'ni_connection_point_connection_point_id': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'connection_point_id': 'network-instances/network-instance/connection-points/connection-point/connection-point-id',
            }
        ],
        'ni_connection_point_endpoint_id': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'connection_point_id': 'network-instances/network-instance/connection-points/connection-point/connection-point-id',
                'endpoint_id': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/endpoint-id',
            }
        ],
        'ni_connection_point_precedence': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'connection_point_id': 'network-instances/network-instance/connection-points/connection-point/connection-point-id',
                'endpoint_id': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/endpoint-id',
                'precedence': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config/precedence',
            }
        ],
        'ni_connection_point_type': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'connection_point_id': 'network-instances/network-instance/connection-points/connection-point/connection-point-id',
                'endpoint_id': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/endpoint-id',
                'cp_type': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config/type',
            }
        ],
        'ni_connection_point_remote_system': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'connection_point_id': 'network-instances/network-instance/connection-points/connection-point/connection-point-id',
                'endpoint_id': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/endpoint-id',
                'cp_type': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config/type',
                'remote_system': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/config/remote-system',
            }
        ],
        'ni_connection_point_site_id': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'connection_point_id': 'network-instances/network-instance/connection-points/connection-point/connection-point-id',
                'endpoint_id': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/endpoint-id',
                'cp_type': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config/type',
                'site_id': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/config/site-id',
            }
        ],
        'ni_connection_point_virtual_circuit_identifier': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'connection_point_id': 'network-instances/network-instance/connection-points/connection-point/connection-point-id',
                'endpoint_id': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/endpoint-id',
                'cp_type': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config/type',
                'virtual_circuit_identifier': 'network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/config/virtual-circuit-identifier',
            }
        ],
        'ni_encapsulation_encapsulation_type': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'encapsulation_type': 'network-instances/network-instance/encapsulation/config/encapsulation-type',
            }
        ],
        'ni_encapsulation_label_allocation_mode': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'label_allocation_mode': 'network-instances/network-instance/encapsulation/config/label-allocation-mode',
            }
        ],
        'ni_fdb_mac_aging_time': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'mac_aging_time': 'network-instances/network-instance/fdb/config/mac-aging-time',
            }
        ],
        'ni_fdb_mac_learning': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'mac_learning': 'network-instances/network-instance/fdb/config/mac-learning',
            }
        ],
        'ni_fdb_maximum_entries': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'maximum_entries': 'network-instances/network-instance/fdb/config/maximum-entries',
            }
        ],
        'ni_t_ldp_afi_name': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'afi_name': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/afi-name',
            }
        ],
        'ni_t_ldp_remote_address': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'afi_name': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/afi-name',
                'remote_address': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/targets/target/remote-address',
            }
        ],
        'ni_t_ldp_local_address': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'afi_name': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/afi-name',
                'remote_address': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/targets/target/remote-address',
                'local_address': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/targets/target/config/local-address',
            }
        ],
        'ni_t_ldp_enabled': [
            {
                'name': 'network-instances/network-instance/name',
                'type': 'network-instances/network-instance/config/type',
                'afi_name': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/afi-name',
                'remote_address': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/targets/target/remote-address',
                'enabled': 'network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family/targets/target/config/enabled',
            }
        ],
        'ni_bgp_as': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
            }
        ],
        'ni_bgp_router_id': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'router_id': 'network-instances/network-instance/protocols/protocol/bgp/global/config/router-id',
            }
        ],
        'ni_bgp_neighbor_address': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
            }
        ],
        'ni_bgp_peer_as': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'peer_as': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config/peer-as',
            }
        ],
        'ni_bgp_local_as': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'peer_as': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config/peer-as',
                'local_as': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config/local-as',
            }
        ],
        'ni_bgp_peer_type': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'peer_type': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config/peer-type',
            }
        ],
        'ni_bgp_remove_private_as': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'remove_private_as': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config/remove-private-as',
            }
        ],
        'ni_bgp_description': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'description': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config/description',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'peer_as': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config/peer-as',
            }
        ],
        'ni_bgp_enabled': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'enabled': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/ebgp-multihop/config/enabled',
            }
        ],
        'ni_bgp_multihop_ttl': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'peer_as': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/config/peer-as',
                'as': 'network-instances/network-instance/protocols/protocol/bgp/global/config/as',
                'multihop_ttl': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/ebgp-multihop/config/multihop-ttl',
            }
        ],
        'ni_bgp_import_policy': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
            },
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'import_export_bgp_policy': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/apply-policy/config/import-policy',
            },
        ],
        'ni_bgp_export_policy': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
            },
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'neighbor_address': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/neighbor-address',
                'import_export_bgp_policy': 'network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/apply-policy/config/export-policy',
            },
        ],
        'ni_protocol_instances_creation': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
            }
        ],
        'ni_protocol_instances_enabled': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'enabled': 'network-instances/network-instance/protocols/protocol/config/enabled',
            }
        ],
        'ni_ospf_router_id': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'router_id': 'network-instances/network-instance/protocols/protocol/ospfv2/global/config/router-id',
            }
        ],
        'ni_ospf_identifier': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'area_identifier': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/identifier',
            }
        ],
        'ni_ospf_id': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'area_identifier': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/identifier',
                'id': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/id',
            }
        ],
        'ni_ospf_network_type': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'area_identifier': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/identifier',
                'id': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/id',
                'network_type': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/config/network-type',
            }
        ],
        'ni_ospf_authentication_type': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'area_identifier': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/identifier',
                'id': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/id',
                'authentication_type': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/config/authentication-type',
            }
        ],
        'ni_ospf_passive': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'area_identifier': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/identifier',
                'id': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/id',
                'passive': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/config/passive',
            }
        ],
        'ni_ospf_interface': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'area_identifier': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/identifier',
                'id': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/id',
                'interface': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/interface-ref/config/interface',
            }
        ],
        'ni_ospf_subinterface': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
            },
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'area_identifier': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/identifier',
                'id': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/id',
                'interface': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/interface-ref/config/interface',
                'subinterface': 'network-instances/network-instance/protocols/protocol/ospfv2/areas/area/interfaces/interface/interface-ref/config/subinterface',
            }
        ],
        'ni_rt_policy_import_policy': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
            },
            {
                'name': 'network-instances/network-instance/name',
                'import_policy': 'network-instances/network-instance/inter-instance-policies/apply-policy/config/import-policy',
            }
        ],
        'ni_rt_policy_export_policy': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
            },
            {
                'name': 'network-instances/network-instance/name',
                'export_policy': 'network-instances/network-instance/inter-instance-policies/apply-policy/config/export-policy',
            }
        ],
        'ni_static_prefix': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'prefix': 'network-instances/network-instance/protocols/protocol/static-routes/static/prefix',
            }
        ],
        'ni_next_hop': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'prefix': 'network-instances/network-instance/protocols/protocol/static-routes/static/prefix',
                'index': 'network-instances/network-instance/protocols/protocol/static-routes/static/next-hops/next-hop/index',
                'next_hop': 'network-instances/network-instance/protocols/protocol/static-routes/static/next-hops/next-hop/config/next-hop',
            }
        ],
        'ni_metric': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'prefix': 'network-instances/network-instance/protocols/protocol/static-routes/static/prefix',
                'index': 'network-instances/network-instance/protocols/protocol/static-routes/static/next-hops/next-hop/index',
                'metric': 'network-instances/network-instance/protocols/protocol/static-routes/static/next-hops/next-hop/config/metric',
            }
        ],
        'ni_protocols_tables_creation': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier': 'network-instances/network-instance/protocols/protocol/identifier',
                'protocol_name': 'network-instances/network-instance/protocols/protocol/name',
                'address_family': 'network-instances/network-instance/tables/table/address-family',
            }
        ],
        'ni_protocol_tables_connection': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier_dst_protocol': 'network-instances/network-instance/table-connections/table-connection/dst-protocol',
                'identifier_src_protocol': 'network-instances/network-instance/table-connections/table-connection/src-protocol',
                'address_family': 'network-instances/network-instance/table-connections/table-connection/address-family',
            }
        ],
        'ni_protocol_tables_connection_default_import_policy': [
            {
                'name': 'network-instances/network-instance/name',
                'identifier_dst_protocol': 'network-instances/network-instance/table-connections/table-connection/dst-protocol',
                'identifier_src_protocol': 'network-instances/network-instance/table-connections/table-connection/src-protocol',
                'address_family': 'network-instances/network-instance/table-connections/table-connection/address-family',
                'default_import_policy': 'network-instances/network-instance/table-connections/table-connection/config/default-import-policy',
            }
        ],
        'ni_interface_id': [
            {
                'name': 'network-instances/network-instance/name',
                'id': 'network-instances/network-instance/interfaces/interface/id',
            }
        ],
        'ni_interface_interface': [
            {
                'name': 'network-instances/network-instance/name',
                'id': 'network-instances/network-instance/interfaces/interface/id',
                'interface': 'network-instances/network-instance/interfaces/interface/config/interface',
            }
        ],
        'ni_interface_subinterface': [
            {
                'interface_name': 'interfaces/interface/name',
                'index': 'interfaces/interface/subinterfaces/subinterface/index',
            },
            {
                'name': 'network-instances/network-instance/name',
                'id': 'network-instances/network-instance/interfaces/interface/id',
                'interface': 'network-instances/network-instance/interfaces/interface/config/interface',
                'subinterface': 'network-instances/network-instance/interfaces/interface/config/subinterface',
            }
        ],
        'ni_protocol_tables_connection_import_policy': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
            },
            {
                'name': 'network-instances/network-instance/name',
                'identifier_src_protocol': 'network-instances/network-instance/table-connections/table-connection/src-protocol',
                'identifier_dst_protocol': 'network-instances/network-instance/table-connections/table-connection/dst-protocol',
                'address_family': 'network-instances/network-instance/table-connections/table-connection/address-family',
                'import_policy': 'network-instances/network-instance/table-connections/table-connection/config/import-policy',
            }
        ]
    }

    def execute_network_instance_edit_config_test_case(self):
        filter_to_use = """
                    <filter>
                        <network-instances xmlns="http://openconfig.net/yang/network-instance">
                        <network-instance>
                        <name>{}</name>
                        </network-instance>
                        </network-instances>
                    </filter>
                    """
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=self.rpc_idx_in_test_case,
                                                                      variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()

    def execute_rpc(self):
        if self.rpcs_list[self.rpc_idx_in_test_case]['operation'] == 'edit-config':
            self.execute_network_instance_edit_config_test_case()
        elif self.rpcs_list[self.rpc_idx_in_test_case]['operation'] == 'get':
            self.execute_get_test_case_with_dispatch()


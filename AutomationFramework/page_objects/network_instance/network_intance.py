from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class NetworkInstance(BasePageObject):
    variables_paths = {
        'ni_config_name': [
            {
                'name': 'network-instances/network-instance/name',
                'instance_name': 'network-instances/network-instance/config/name'
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
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=0, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()

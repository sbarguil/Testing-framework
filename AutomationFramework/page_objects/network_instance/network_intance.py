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

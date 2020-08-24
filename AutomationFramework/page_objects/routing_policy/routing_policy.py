from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class RoutingPolicy(BasePageObject):
    variables_paths = {
        'rp_community_def_ext_community_member': [
            {
                'ext_community_set_name': 'routing-policy/defined-sets/bgp-defined-sets/ext-community-sets/ext-community-set/ext-community-set-name',
                'ext_community_member': 'routing-policy/defined-sets/bgp-defined-sets/ext-community-sets/ext-community-set/config/ext-community-member',
            }
        ],
        'rp_community_def_ext_community_set_name': [
            {
                'ext_community_set_name': 'routing-policy/defined-sets/bgp-defined-sets/ext-community-sets/ext-community-set/ext-community-set-name',
            }
        ],
    }

    def execute_rp_community_def_edit_config_test_case(self):
        filter_to_use = """
                    <filter>
                        <routing-policy xmlns="http://openconfig.net/yang/routing-policy">
                            <defined-sets>
                              <bgp-defined-sets xmlns="http://openconfig.net/yang/bgp-policy">
                                <ext-community-sets>
                                  <ext-community-set>
                                    <ext-community-set-name>{}</ext-community-set-name>
                                  </ext-community-set>
                                </ext-community-sets>
                              </bgp-defined-sets>
                            </defined-sets>
                          </routing-policy>
                    </filter>
                    """
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=0, variable='ext_community_set_name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()

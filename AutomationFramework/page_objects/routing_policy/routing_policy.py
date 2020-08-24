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
        'rp_policy_def_name': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
            }
        ],
        'rp_policy_def_policy_result': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
                'statement_name': 'routing-policy/policy-definitions/policy-definition/statements/statement/name',
                'policy_result': 'routing-policy/policy-definitions/policy-definition/statements/statement/actions/config/policy-result',
            }
        ],
        'rp_policy_def_install_protocol_eq': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
                'statement_name': 'routing-policy/policy-definitions/policy-definition/statements/statement/name',
                'install_protocol_eq': 'routing-policy/policy-definitions/policy-definition/statements/statement/conditions/config/install-protocol-eq',
            }
        ],
        'rp_policy_def_match_set_options': [
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
                'statement_name': 'routing-policy/policy-definitions/policy-definition/statements/statement/name',
                'match_set_options': 'routing-policy/policy-definitions/policy-definition/statements/statement/conditions/bgp-conditions/match-ext-community-set/config/match-set-options',
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

    def execute_rp_policy_def_edit_config_test_case(self):
        filter_to_use = """
                    <filter>
                        <routing-policy xmlns="http://openconfig.net/yang/routing-policy">
                            <policy-definitions>
                              <policy-definition>
                                <name>{}</name>
                              </policy-definition>
                            </policy-definitions>
                        </routing-policy>
                    </filter>
                    """
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=0, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()

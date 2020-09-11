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
<<<<<<< HEAD
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
=======
        'rp_policy_def_match_set_options': [
            {
                'ext_community_set_name': 'routing-policy/defined-sets/bgp-defined-sets/ext-community-sets/ext-community-set/ext-community-set-name',
                'ext_community_member': 'routing-policy/defined-sets/bgp-defined-sets/ext-community-sets/ext-community-set/config/ext-community-member',
            },
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
                'statement_name': 'routing-policy/policy-definitions/policy-definition/statements/statement/name',
                'ext_community_set': 'routing-policy/policy-definitions/policy-definition/statements/statement/conditions/bgp-conditions/match-ext-community-set/config/ext-community-set',
                'match_set_options': 'routing-policy/policy-definitions/policy-definition/statements/statement/conditions/bgp-conditions/match-ext-community-set/config/match-set-options',
            }
        ],
        'rp_policy_def_ext_community_set': [
            {
                'ext_community_set_name': 'routing-policy/defined-sets/bgp-defined-sets/ext-community-sets/ext-community-set/ext-community-set-name',
                'ext_community_member': 'routing-policy/defined-sets/bgp-defined-sets/ext-community-sets/ext-community-set/config/ext-community-member',
            },
            {
                'name': 'routing-policy/policy-definitions/policy-definition/name',
                'statement_name': 'routing-policy/policy-definitions/policy-definition/statements/statement/name',
                'ext_community_set': 'routing-policy/policy-definitions/policy-definition/statements/statement/conditions/bgp-conditions/match-ext-community-set/config/ext-community-set',
            }
        ],
>>>>>>> 7baf719bb03a924716cbd342738ffd7980fba964
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
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=self.rpc_idx_in_test_case,
                                                                      variable='ext_community_set_name')
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
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=self.rpc_idx_in_test_case, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()

    def execute_rpc(self):
        if self.rpcs_list[self.rpc_idx_in_test_case]['operation'] == 'edit-config':
            self.execute_rp_policy_def_edit_config_test_case()
        elif self.rpcs_list[self.rpc_idx_in_test_case]['operation'] == 'get':
            self.execute_get_test_case_with_dispatch()

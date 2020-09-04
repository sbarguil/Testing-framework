import pytest
from AutomationFramework.page_objects.routing_policy.routing_policy import RoutingPolicy
from AutomationFramework.tests.base_test import BaseTest


class TestRPPolicyDef(BaseTest):
    test_case_file = 'rp_policy_def.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_policy_def_name',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_policy_def_name(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_policy_def_policy_result',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_policy_def_policy_result(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_policy_def_install_protocol_eq',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_policy_def_install_protocol_eq(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason="Error, tag bgp-conditions not known. ncclient.operations.rpc.RPCError: {'type': 'application', 'tag': 'unknown-element', 'app_tag': None, 'severity': 'error', 'info': '<?xml version=1.0 encoding=UTF-8?><error-info xmlns=urn:ietf:params:xml:ns:netconf:base:1.0><bad-element>match-ext-community-set</bad-element>\n</error-info>\n', 'path': '\n    /rpc/edit-config/config/oc-rpol:routing-policy/oc-rpol:policy-definitions/oc-rpol:policy-definition/oc-rpol:statements/oc-rpol:statement/oc-rpol:conditions/oc-bgp-pol:bgp-conditions\n  ', 'message': None}")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_policy_def_match_set_options',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_policy_def_match_set_options(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

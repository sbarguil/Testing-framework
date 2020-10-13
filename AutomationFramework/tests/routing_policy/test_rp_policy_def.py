import pytest
from AutomationFramework.page_objects.routing_policy.routing_policy import RoutingPolicy
from AutomationFramework.tests.base_test import BaseTest


class TestRPPolicyDef(BaseTest):
    test_case_file = 'rp_policy_def.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_policy_def_name',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_policy_def_name(self, create_page_object):
        create_page_object.execute_rp_policy_def_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_policy_def_policy_result',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_policy_def_policy_result(self, create_page_object):
        create_page_object.execute_rp_policy_def_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_policy_def_install_protocol_eq',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_policy_def_install_protocol_eq(self, create_page_object):
        create_page_object.execute_rp_policy_def_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'rp_policy_def_match_set_options',
                                                                   'page_object_rpcs_classes': [RoutingPolicy,
                                                                                                RoutingPolicy],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_rp_policy_def_match_set_options(self, multiple_create_page_objects):
        multiple_create_page_objects[0].execute_rp_community_def_edit_config_test_case()
        assert multiple_create_page_objects[0].validate_rpc(), multiple_create_page_objects[0].get_test_case_description()
        multiple_create_page_objects[1].execute_rp_policy_def_edit_config_test_case()
        assert multiple_create_page_objects[1].validate_rpc(), multiple_create_page_objects[1].get_test_case_description()

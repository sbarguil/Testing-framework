import pytest
from AutomationFramework.page_objects.routing_policy.routing_policy import RoutingPolicy
from AutomationFramework.tests.base_test import BaseTest


class TestRPCommunityDef(BaseTest):
    test_case_file = 'rp_community_def.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_community_def_ext_community_member',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_community_def_ext_community_member(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'rp_community_def_ext_community_set_name',
                                                         'page_object_class': RoutingPolicy}])
    def test_rp_community_def_ext_community_set_name(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

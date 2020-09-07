import pytest
from AutomationFramework.page_objects.network_instance.network_intance import NetworkInstance
from AutomationFramework.page_objects.routing_policy.routing_policy import RoutingPolicy
from AutomationFramework.tests.base_test import BaseTest


class TestNetworkInstanceRTPolicy(BaseTest):
    test_case_file = 'ni_rt_policy.yml'

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'ni_rt_policy_import_policy',
                                                                   'page_object_rpcs_classes': [RoutingPolicy,
                                                                                                NetworkInstance],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_ni_rt_policy_import_policy(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'ni_rt_policy_export_policy',
                                                                   'page_object_rpcs_classes': [RoutingPolicy,
                                                                                                NetworkInstance],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_ni_rt_policy_export_policy(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

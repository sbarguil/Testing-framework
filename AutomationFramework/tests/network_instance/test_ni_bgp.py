import pytest
from AutomationFramework.page_objects.network_instance.network_intance import NetworkInstance
from AutomationFramework.page_objects.routing_policy.routing_policy import RoutingPolicy
from AutomationFramework.tests.base_test import BaseTest


class TestNetworkInstanceBGP(BaseTest):
    test_case_file = 'ni_bgp.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_as',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_as(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_router_id',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_router_id(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_neighbor_address',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_neighbor_address(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_peer_as',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_peer_as(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_local_as',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_local_as(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_peer_type',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_peer_type(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_remove_private_as',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_remove_private_as(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_description',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_description(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_enabled',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_enabled(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_bgp_multihop_ttl',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_bgp_multihop_ttl(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'ni_bgp_import_policy',
                                                                   'page_object_rpcs_classes': [RoutingPolicy,
                                                                                                NetworkInstance],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_ni_bgp_import_policy(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'ni_bgp_export_policy',
                                                                   'page_object_rpcs_classes': [RoutingPolicy,
                                                                                                NetworkInstance],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_ni_bgp_export_policy(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

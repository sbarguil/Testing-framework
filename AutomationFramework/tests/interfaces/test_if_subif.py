import pytest
from AutomationFramework.page_objects.interfaces.interfaces import Interfaces
from AutomationFramework.tests.base_test import BaseTest


class TestInterfacesSubInterfaces(BaseTest):
    test_case_file = 'if_subif.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_description',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_description(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_enabled',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_enabled(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_ip_prefix_length',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_ip_prefix_length(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'if_subif_ip_state',
                                                                   'page_object_rpcs_classes': [Interfaces, Interfaces],
                                                                   'rpc_clean_order': None,
                                                                   }])
    def test_if_subif_ip_state(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_interface_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'if_subif_origin',
                                                                   'page_object_rpcs_classes': [Interfaces, Interfaces],
                                                                   'rpc_clean_order': None,
                                                                   }])
    def test_if_subif_origin(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_interface_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_dhcp_client',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_dhcp_client(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_mtu',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_mtu(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_vlan_id',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_vlan_id(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_inner_outer_vlan_id',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_inner_outer_vlan_id(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_match_vlan_id',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_match_vlan_id(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

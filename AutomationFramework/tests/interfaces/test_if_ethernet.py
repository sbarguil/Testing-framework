import pytest
from AutomationFramework.page_objects.interfaces.interfaces import Interfaces
from AutomationFramework.tests.base_test import BaseTest


class TestInterfacesEthernet(BaseTest):
    test_case_file = 'if_ethernet.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_ethernet_auto_negotiate',
                                                         'page_object_class': Interfaces}])
    def test_if_ethernet_auto_negotiate(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_ethernet_duplex_mode',
                                                         'page_object_class': Interfaces}])
    def test_if_ethernet_duplex_mode(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_ethernet_port_speed',
                                                         'page_object_class': Interfaces}])
    def test_if_ethernet_port_speed(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'if_ethernet_aggregate_id',
                                                                   'page_object_rpcs_classes': [Interfaces, Interfaces],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_if_ethernet_aggregate_id(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_interface_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_ethernet_port_speed_state',
                                                         'page_object_class': Interfaces}])
    def test_if_ethernet_port_speed_state(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

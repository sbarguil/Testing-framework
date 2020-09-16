import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.page_objects.interfaces.interfaces import Interfaces
from AutomationFramework.tests.base_test import BaseTest


class TestHardwarePort(BaseTest):
    test_case_file = 'hw_port.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_port_channel_speed',
                                                         'page_object_class': Hardware}])
    def test_hw_port_channel_speed(self, create_page_object):
        create_page_object.execute_hardware_component_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_port_num_channels',
                                                         'page_object_class': Hardware}])
    def test_hw_port_num_channels(self, create_page_object):
        create_page_object.execute_hardware_component_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'hw_port_channel_speed_state',
                                                                   'page_object_rpcs_classes': [Hardware, Hardware],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_hw_port_channel_speed_state(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'hw_port_num_channels_state',
                                                                   'page_object_rpcs_classes': [Hardware, Hardware],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_hw_port_num_channels_state(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.tests.base_test import BaseTest


class TestHardwareConfig(BaseTest):
    test_case_file = 'hw_config.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_config_name',
                                                         'page_object_class': Hardware}])
    def test_hw_config_name(self, create_page_object):
        create_page_object.execute_hardware_component_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

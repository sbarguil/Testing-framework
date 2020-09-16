import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.tests.base_test import BaseTest


class TestHardwareSubcomponent(BaseTest):
    test_case_file = 'hw_subcomponent.yml'

    # Needs to be reviwed
    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'hw_subcomponent_name',
                                                                   'page_object_rpcs_classes': [Hardware, Hardware,
                                                                                                Hardware],
                                                                   'rpc_clean_order': [2, 1, 0],
                                                                   }])
    def test_hw_subcomponent_name(self, multiple_create_page_objects):
        for page_object in multiple_create_page_objects:
            page_object.execute_hardware_rpc()
            assert page_object.validate_rpc(), page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_subcomponent_name_state',
                                                         'page_object_class': Hardware}])
    def test_hw_subcomponent_name_state(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

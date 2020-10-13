import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.tests.base_test import BaseTest


class TestHardwareProperties(BaseTest):
    test_case_file = 'hw_properties.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_properties_name',
                                                         'page_object_class': Hardware}])
    def test_hw_properties_name(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_properties_value',
                                                         'page_object_class': Hardware}])
    def test_hw_properties_value(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

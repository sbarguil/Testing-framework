import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.tests.base_test import BaseTest


class TestHardwareLinecard(BaseTest):
    test_case_file = 'hw_linecard.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_linecard_power_admin',
                                                         'page_object_class': Hardware}])
    def test_hw_linecard_power_admin(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_linecard_power_admin_state',
                                                         'page_object_class': Hardware}])
    def test_hw_linecard_power_admin_state(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

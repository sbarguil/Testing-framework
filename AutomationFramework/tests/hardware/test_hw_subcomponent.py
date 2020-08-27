import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.tests.base_test import BaseTest


class TestHardwareSubcomponent(BaseTest):
    test_case_file = 'hw_subcomponent.yml'

    @pytest.mark.skip(
        reason='We need to create a component for the aggregate it as a subcomponent of another component')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_subcomponent_name',
                                                         'page_object_class': Hardware}])
    def test_hw_subcomponent_name(self, create_page_object):
        create_page_object.execute_hardware_component_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(
        reason='We need to create a component for the aggregate it as a subcomponent of another component and the get operation')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_subcomponent_name_state',
                                                         'page_object_class': Hardware}])
    def test_hw_subcomponent_name_state(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

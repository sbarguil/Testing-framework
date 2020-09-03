import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.tests.base_test import BaseTest


class TestHardwarePSU(BaseTest):
    test_case_file = 'hw_psu.yml'

    @pytest.mark.skip(reason='Not tested. There are no power supply units to test')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_psu_enabled',
                                                         'page_object_class': Hardware}])
    def test_hw_psu_enabled(self, create_page_object):
        create_page_object.execute_hardware_component_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Not tested. There are no power supply units to test')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_psu_capacity',
                                                         'page_object_class': Hardware}])
    def test_hw_psu_capacity(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Not tested. There are no power supply units to test')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_psu_enabled_state',
                                                         'page_object_class': Hardware}])
    def test_hw_psu_enabled_state(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Not tested. There are no power supply units to test')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_psu_input_voltage',
                                                         'page_object_class': Hardware}])
    def test_hw_psu_input_voltage(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Not tested. There are no power supply units to test')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_psu_output_current',
                                                         'page_object_class': Hardware}])
    def test_hw_psu_output_current(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Not tested. There are no power supply units to test')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_psu_output_power',
                                                         'page_object_class': Hardware}])
    def test_hw_psu_output_power(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Not tested. There are no power supply units to test')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_psu_output_voltage',
                                                         'page_object_class': Hardware}])
    def test_hw_psu_output_voltage(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Not tested. There are no power supply units to test')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_psu_input_current',
                                                         'page_object_class': Hardware}])
    def test_hw_psu_input_current(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

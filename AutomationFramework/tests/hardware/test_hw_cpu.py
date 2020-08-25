import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.tests.base_test import BaseTest


class TestHardwareCPU(BaseTest):
    test_case_file = 'hw_cpu.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_cpu_avg',
                                                         'page_object_class': Hardware}])
    def test_hw_cpu_avg(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_cpu_instant',
                                                         'page_object_class': Hardware}])
    def test_hw_cpu_instant(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_cpu_interval',
                                                         'page_object_class': Hardware}])
    def test_hw_cpu_interval(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_cpu_max',
                                                         'page_object_class': Hardware}])
    def test_hw_cpu_max(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_cpu_max_time',
                                                         'page_object_class': Hardware}])
    def test_hw_cpu_max_time(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_cpu_min',
                                                         'page_object_class': Hardware}])
    def test_hw_cpu_min(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_cpu_min_time',
                                                         'page_object_class': Hardware}])
    def test_hw_cpu_min_time(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

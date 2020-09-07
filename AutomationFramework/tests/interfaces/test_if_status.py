import pytest
from AutomationFramework.page_objects.interfaces.interfaces import Interfaces
from AutomationFramework.tests.base_test import BaseTest


class TestInterfacesStatus(BaseTest):
    test_case_file = 'if_status.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_status_admin_status',
                                                         'page_object_class': Interfaces}])
    def test_if_status_admin_status(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_status_enabled',
                                                         'page_object_class': Interfaces}])
    def test_if_status_enabled(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_status_name',
                                                         'page_object_class': Interfaces}])
    def test_if_status_name(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_status_oper_status',
                                                         'page_object_class': Interfaces}])
    def test_if_status_oper_status(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

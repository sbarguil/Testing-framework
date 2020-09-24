import pytest
from AutomationFramework.page_objects.interfaces.interfaces import Interfaces
from AutomationFramework.tests.base_test import BaseTest


class TestInterfacesConfig(BaseTest):
    test_case_file = 'if_config.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_config_description',
                                                         'page_object_class': Interfaces}])
    def test_if_config_description(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_config_enabled',
                                                         'page_object_class': Interfaces}])
    def test_if_config_enabled(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_config_loopback_mode',
                                                         'page_object_class': Interfaces}])
    def test_if_config_loopback_mode(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_config_mtu',
                                                         'page_object_class': Interfaces}])
    def test_if_config_mtu(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_config_tpid',
                                                         'page_object_class': Interfaces}])
    def test_if_config_tpid(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_config_type',
                                                         'page_object_class': Interfaces}])
    def test_if_config_type(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

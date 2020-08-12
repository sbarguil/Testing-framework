import pytest

from AutomationFramework.page_objects.interfaces.interfaces import Interfaces


class TestInterfacesConfig:
    test_case_file = 'if_config.yml'

    def test_if_config_description(self):
        interfaces_page = Interfaces(test_case_file=self.test_case_file, test_case_name='if_config_description')
        interfaces_page.execute_edit_config_test_case()
        assert interfaces_page.validate_test_case_params(), interfaces_page.get_test_case_description()

    def test_if_config_enabled(self):
        interfaces_page = Interfaces(test_case_file=self.test_case_file, test_case_name='if_config_enabled')
        interfaces_page.execute_edit_config_test_case()
        assert interfaces_page.validate_test_case_params(), interfaces_page.get_test_case_description()

    @pytest.mark.skip(reason="Test not working, Interface not found")
    def test_if_config_loopback_mode(self):
        interfaces_page = Interfaces(test_case_file=self.test_case_file, test_case_name='if_config_loopback_mode')
        interfaces_page.execute_edit_config_test_case()
        assert interfaces_page.validate_test_case_params(), interfaces_page.get_test_case_description()

    def test_if_config_mtu(self):
        interfaces_page = Interfaces(test_case_file=self.test_case_file, test_case_name='if_config_mtu')
        interfaces_page.execute_edit_config_test_case()
        assert interfaces_page.validate_test_case_params(), interfaces_page.get_test_case_description()

    @pytest.mark.skip(reason="Cisco doesn't have the param, test in juniper ")
    def test_if_config_tpid(self):
        interfaces_page = Interfaces(test_case_file=self.test_case_file, test_case_name='if_config_tpid')
        interfaces_page.execute_edit_config_test_case()
        assert interfaces_page.validate_test_case_params(), interfaces_page.get_test_case_description()

    @pytest.mark.skip(reason="Test not working, fix by getting the prefix from the first get config and change the yaml"
                             "by sending just the value without prefix")
    def test_if_config_type(self):
        interfaces_page = Interfaces(test_case_file=self.test_case_file, test_case_name='if_config_type')
        interfaces_page.execute_edit_config_test_case()
        assert interfaces_page.validate_test_case_params(), interfaces_page.get_test_case_description()

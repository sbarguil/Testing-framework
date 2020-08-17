import pytest
from AutomationFramework.page_objects.interfaces.interfaces import Interfaces
from AutomationFramework.tests.base_test import BaseTest


class TestInterfacesGre(BaseTest):
    test_case_file = 'if_gre.yml'

    @pytest.mark.skip(reason="It seams devices doesn't support the creation of gre tunnels")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_gre_dst',
                                                         'page_object_class': Interfaces}])
    def test_if_gre_dst(self, create_page_object):
        create_page_object.execute_interfaces_edit_config_test_case()
        assert create_page_object.validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason="It seams devices doesn't support the creation of gre tunnels")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_gre_src',
                                                         'page_object_class': Interfaces}])
    def test_if_gre_src(self, create_page_object):
        create_page_object.execute_interfaces_edit_config_test_case()
        assert create_page_object.validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason="It seams devices doesn't support the creation of gre tunnels")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_gre_ttl',
                                                         'page_object_class': Interfaces}])
    def test_if_gre_ttl(self, create_page_object):
        create_page_object.execute_interfaces_edit_config_test_case()
        assert create_page_object.validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason="It seams devices doesn't support the creation of gre tunnels")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_gre_ip_prefix_length',
                                                         'page_object_class': Interfaces}])
    def test_if_gre_ip_prefix_length(self, create_page_object):
        create_page_object.execute_interfaces_edit_config_test_case()
        assert create_page_object.validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason="It seams devices doesn't support the creation of gre tunnels")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_gre_mtu',
                                                         'page_object_class': Interfaces}])
    def test_if_gre_mtu(self, create_page_object):
        create_page_object.execute_interfaces_edit_config_test_case()
        assert create_page_object.validate_test_case_params(), create_page_object.get_test_case_description()

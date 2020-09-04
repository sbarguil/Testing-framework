import pytest
from AutomationFramework.page_objects.network_instance.network_intance import NetworkInstance
from AutomationFramework.tests.base_test import BaseTest


class TestNetworkInstanceTLDP(BaseTest):
    test_case_file = 'ni_t_ldp.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_t_ldp_afi_name',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_t_ldp_afi_name(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_t_ldp_remote_address',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_t_ldp_remote_address(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_t_ldp_local_address',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_t_ldp_local_address(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_t_ldp_enabled',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_t_ldp_enabled(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

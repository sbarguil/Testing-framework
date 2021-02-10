import pytest

from AutomationFramework.page_objects.interfaces.interfaces import Interfaces
from AutomationFramework.page_objects.network_instance.network_intance import NetworkInstance
from AutomationFramework.tests.base_test import BaseTest


class TestNetworkInstanceOSPF(BaseTest):
    test_case_file = 'ni_ospf.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_ospf_router_id',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_ospf_router_id(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_ospf_identifier',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_ospf_identifier(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_ospf_id',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_ospf_id(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_ospf_authentication_type',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_ospf_authentication_type(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_ospf_passive',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_ospf_passive(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_ospf_interface',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_ospf_interface(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'ni_ospf_subinterface',
                                                                   'page_object_rpcs_classes': [Interfaces,
                                                                                                NetworkInstance],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_ni_ospf_subinterface(self, multiple_create_page_objects):
        multiple_create_page_objects[0].execute_interface_rpc()
        assert multiple_create_page_objects[0].validate_rpc(), multiple_create_page_objects[0].get_test_case_description()
        multiple_create_page_objects[1].execute_network_instance_edit_config_test_case()
        assert multiple_create_page_objects[1].validate_rpc(), multiple_create_page_objects[1].get_test_case_description()

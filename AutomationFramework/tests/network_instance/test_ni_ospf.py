import pytest
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

    @pytest.mark.skip(reason="It needs a subinterface to be referenced. error: ncclient.operations.rpc.RPCError: illegal reference /network-instances/network-instance[name='Prueba_LxVPN']/protocols/protocol[identifier='oc-pol-types:OSPF'][name='OSPF_1']/ospfv2/areas/area[identifier='0.0.0.0']/interfaces/interface[id='1']/interface-ref/config/subinterface")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_ospf_subinterface',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_ospf_subinterface(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

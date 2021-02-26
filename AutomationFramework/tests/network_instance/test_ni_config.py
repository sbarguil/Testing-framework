import pytest
from AutomationFramework.page_objects.network_instance.network_intance import NetworkInstance
from AutomationFramework.tests.base_test import BaseTest


class TestNetworkInstanceConfig(BaseTest):
    test_case_file = 'ni_config.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_config_name',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_config_name(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()
        
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_get_name',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_get_name(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_config_type',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_config_type(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_config_enabled',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_config_enabled(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_config_description',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_config_description(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_config_router_id',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_config_router_id(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_config_route_distinguisher',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_config_route_distinguisher(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    # I added the type param, if not added an error raises. ncclient.operations.rpc.RPCError: /network-instances/network-instance[name='Prueba_LxVPN']/config/enabled-address-families[.='oc-types:IPV4']: the 'when' expression "./type = 'oc-ni-types:L3VRF' or ./type = 'oc-ni-types:L2L3'" failed
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_config_enabled_address_families',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_config_enabled_address_families(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    # I added the type param, if not added an error raises. ncclient.operations.rpc.RPCError: /network-instances/network-instance[name='Prueba_LxVPN']/config/mtu: the 'when' expression "./type = 'oc-ni-types:L2VSI' or ./type = 'oc-ni-types:L2P2P' or ./type = 'oc-ni-types:L2L3'" failed
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_config_mtu',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_config_mtu(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

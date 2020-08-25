import pytest
from AutomationFramework.page_objects.interfaces.interfaces import Interfaces
from AutomationFramework.tests.base_test import BaseTest


class TestInterfacesSubInterfaces(BaseTest):
    test_case_file = 'if_subif.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_type',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_type(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_description',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_description(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_enabled',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_enabled(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_ip_prefix_length',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_ip_prefix_length(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Before a get to the ip, the subinterface has to be created, so it needs another rpc')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_ip_state',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_ip_state(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Before a get to the origin, the subinterface has to be created, so it needs another rpc')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_origin',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_origin(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason="An exception has occurred when performing the edit_config operation. ncclient.operations.rpc.RPCError: {'type': 'protocol', 'tag': 'unknown-element', 'app_tag': None, 'severity': 'error', 'info': '<?xml version='1.0' encoding='UTF-8'?><error-info xmlns='urn:ietf:params:xml:ns:netconf:base:1.0'><bad-element>rpc</bad-element>\n</error-info>\n', 'path': '\n    /rpc\n  ', 'message': None}")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_dhcp_client',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_dhcp_client(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason="An exception has occurred when performing the edit_config operation. ncclient.operations.rpc.RPCError: {'type': 'protocol', 'tag': 'unknown-element', 'app_tag': None, 'severity': 'error', 'info': '<?xml version='1.0' encoding='UTF-8'?><error-info xmlns='urn:ietf:params:xml:ns:netconf:base:1.0'><bad-element>rpc</bad-element>\n</error-info>\n', 'path': '\n    /rpc\n  ', 'message': None}")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_mtu',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_mtu(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_vlan_id',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_vlan_id(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_inner_outer_vlan_id',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_inner_outer_vlan_id(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'if_subif_match_vlan_id',
                                                         'page_object_class': Interfaces}])
    def test_if_subif_match_vlan_id(self, create_page_object):
        create_page_object.execute_generic_interfaces_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

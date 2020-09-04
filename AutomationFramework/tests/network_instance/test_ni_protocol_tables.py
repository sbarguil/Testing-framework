import pytest
from AutomationFramework.page_objects.network_instance.network_intance import NetworkInstance
from AutomationFramework.tests.base_test import BaseTest


class TestNetworkInstanceProtocolTables(BaseTest):
    test_case_file = 'ni_protocol_tables.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_protocols_tables_creation',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_protocols_tables_creation(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_protocol_tables_connection',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_protocol_tables_connection(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_protocol_tables_connection_default_import_policy',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_protocol_tables_connection_default_import_policy(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

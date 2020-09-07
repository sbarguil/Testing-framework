import pytest
from AutomationFramework.page_objects.network_instance.network_intance import NetworkInstance
from AutomationFramework.tests.base_test import BaseTest


class TestNetworkInstanceFDB(BaseTest):
    test_case_file = 'ni_fdb.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_fdb_mac_aging_time',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_fdb_mac_aging_time(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_fdb_mac_learning',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_fdb_mac_learning(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_fdb_maximum_entries',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_fdb_maximum_entries(self, create_page_object):
        create_page_object.execute_generic_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

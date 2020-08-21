import pytest
from AutomationFramework.page_objects.network_instance.network_intance import NetworkInstance
from AutomationFramework.tests.base_test import BaseTest


class TestNetworkInstanceInterface(BaseTest):
    test_case_file = 'ni_interface.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'ni_interface_id',
                                                         'page_object_class': NetworkInstance}])
    def test_ni_interface_id(self, create_page_object):
        create_page_object.execute_network_instance_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

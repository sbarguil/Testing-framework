import pytest
from AutomationFramework.page_objects.hardware.hardware import Hardware
from AutomationFramework.tests.base_test import BaseTest


class TestHardwareTransceiver(BaseTest):
    test_case_file = 'hw_transceiver.yml'

    @pytest.mark.skip(reason="RPC error: ncclient.operations.rpc.RPCError: /components/component[name='0/0/5-SFP Socket']/oc-transceiver:transceiver: the 'when' expression current()/oc-platform:state/oc-platform:type = 'TRANSCEIVER' failed")
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_transceiver_enabled',
                                                         'page_object_class': Hardware}])
    def test_hw_transceiver_enabled(self, create_page_object):
        create_page_object.execute_hardware_component_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_transceiver_slot_id',
                                                         'page_object_class': Hardware}])
    def test_hw_transceiver_slot_id(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'hw_transceiver_enabled_state',
                                                         'page_object_class': Hardware}])
    def test_hw_transceiver_enabled_state(self, create_page_object):
        create_page_object.execute_get_test_case_with_dispatch()
        assert create_page_object.validate_get_test_case(), create_page_object.get_test_case_description()

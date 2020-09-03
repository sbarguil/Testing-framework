import pytest
from AutomationFramework.page_objects.qos.qos import QOS
from AutomationFramework.tests.base_test import BaseTest


class TestQOSScheduler(BaseTest):
    test_case_file = 'qos_scheduler.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_scheduler_policy_name',
                                                         'page_object_class': QOS}])
    def test_qos_scheduler_policy_name(self, create_page_object):
        create_page_object.execute_qos_scheduler_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_scheduler_sequence',
                                                         'page_object_class': QOS}])
    def test_qos_scheduler_sequence(self, create_page_object):
        create_page_object.execute_qos_scheduler_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_scheduler_id',
                                                         'page_object_class': QOS}])
    def test_qos_scheduler_id(self, create_page_object):
        create_page_object.execute_qos_scheduler_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.skip(reason='Review manually the rpc to see if it works the way it is implemented')
    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_scheduler_queue',
                                                         'page_object_class': QOS}])
    def test_qos_scheduler_queue(self, create_page_object):
        create_page_object.execute_qos_queue_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_scheduler_weight',
                                                         'page_object_class': QOS}])
    def test_qos_scheduler_weight(self, create_page_object):
        create_page_object.execute_qos_scheduler_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_scheduler_cir',
                                                         'page_object_class': QOS}])
    def test_qos_scheduler_cir(self, create_page_object):
        create_page_object.execute_qos_scheduler_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_scheduler_max_queue_depth_bytes',
                                                         'page_object_class': QOS}])
    def test_qos_scheduler_max_queue_depth_bytes(self, create_page_object):
        create_page_object.execute_qos_scheduler_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_scheduler_bc',
                                                         'page_object_class': QOS}])
    def test_qos_scheduler_bc(self, create_page_object):
        create_page_object.execute_qos_scheduler_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

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

    @pytest.mark.parametrize('multiple_create_page_objects_arg', [{'test_case_file': test_case_file,
                                                                   'test_case_name': 'qos_scheduler_queue',
                                                                   'page_object_rpcs_classes': [QOS, QOS],
                                                                   'rpc_clean_order': [1, 0],
                                                                   }])
    def test_qos_scheduler_queue(self, multiple_create_page_objects):
        multiple_create_page_objects[0].execute_qos_queue_edit_config_test_case()
        assert multiple_create_page_objects[0].validate_rpc(), multiple_create_page_objects[0].get_test_case_description()
        multiple_create_page_objects[1].execute_qos_scheduler_edit_config_test_case()
        assert multiple_create_page_objects[1].validate_rpc(), multiple_create_page_objects[1].get_test_case_description()

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

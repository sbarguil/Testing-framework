import pytest
from AutomationFramework.page_objects.qos.qos import QOS
from AutomationFramework.tests.base_test import BaseTest


class TestQOSQueue(BaseTest):
    test_case_file = 'qos_queue.yml'

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_queue_name',
                                                         'page_object_class': QOS}])
    def test_qos_queue_name(self, create_page_object):
        create_page_object.execute_qos_queue_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_queue_minth',
                                                         'page_object_class': QOS}])
    def test_qos_queue_minth(self, create_page_object):
        create_page_object.execute_qos_queue_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

    @pytest.mark.parametrize('create_page_object_arg', [{'test_case_file': test_case_file,
                                                         'test_case_name': 'qos_queue_maxth',
                                                         'page_object_class': QOS}])
    def test_qos_queue_maxth(self, create_page_object):
        create_page_object.execute_qos_queue_edit_config_test_case()
        assert create_page_object.generic_validate_test_case_params(), create_page_object.get_test_case_description()

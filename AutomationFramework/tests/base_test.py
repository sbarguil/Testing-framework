import time
import pytest


class BaseTest:
    @pytest.fixture
    def create_page_object(self, create_page_object_arg):
        test_case_file = create_page_object_arg['test_case_file']
        test_case_name = create_page_object_arg['test_case_name']
        page_object_class = create_page_object_arg['page_object_class']
        test_page_object = page_object_class(test_case_file=test_case_file, test_case_name=test_case_name)
        test_page_object.excel_logger.add_value_to_log_column(value=str(test_page_object.get_test_case_description()),
                                                              column='Test case description')
        test_page_object.excel_logger.add_value_to_log_column(value=str(test_case_name), column='Test case name')
        test_page_object.excel_logger.add_value_to_log_column(value=str(test_page_object.rpc_idx_in_test_case),
                                                              column='RPC ID')
        test_page_object.excel_logger.add_value_to_log_column(value=str(type(test_page_object)), column='POM instance')
        yield test_page_object
        test_page_object.excel_logger.write_log()
        if test_page_object.values_where_changed_after_test:
            test_page_object.clean_after_test()
        time.sleep(3)

    @pytest.fixture
    def multiple_create_page_objects(self, multiple_create_page_objects_arg):
        page_objects_list = []
        rpc_index = 0
        for single_page_object_class in multiple_create_page_objects_arg['page_object_rpcs_classes']:
            test_page_object = single_page_object_class(
                test_case_file=multiple_create_page_objects_arg['test_case_file'],
                test_case_name=multiple_create_page_objects_arg['test_case_name'],
                rpc_idx=rpc_index)

            test_page_object.excel_logger.add_value_to_log_column(value=str(
                test_page_object.get_test_case_description()), column='Test case description')
            test_page_object.excel_logger.add_value_to_log_column(value=str(
                multiple_create_page_objects_arg['test_case_name'],), column='Test case name')
            test_page_object.excel_logger.add_value_to_log_column(value=str(test_page_object.rpc_idx_in_test_case),
                                                                  column='RPC ID')
            test_page_object.excel_logger.add_value_to_log_column(value=str(type(test_page_object)),
                                                                  column='POM instance')
            time.sleep(3)

            page_objects_list.append(test_page_object)
            rpc_index = rpc_index + 1

        yield page_objects_list

        for single_page_object in page_objects_list:
            if single_page_object is not page_objects_list[0]:
                for column in single_page_object.excel_logger.workbook_columns:
                    if column != 'Test case name' and column != 'Test case description':
                        page_objects_list[0].excel_logger.add_value_to_log_column(
                            column=column, value=' \n-------------------\n' +
                                                 single_page_object.excel_logger.log_values[column])
        page_objects_list[0].excel_logger.write_log()

        if multiple_create_page_objects_arg['rpc_clean_order']:
            for rpc_clean_index in multiple_create_page_objects_arg['rpc_clean_order']:
                if page_objects_list[rpc_clean_index].values_where_changed_after_test:
                    page_objects_list[rpc_clean_index].clean_after_test()
                    time.sleep(3)
        else:
            for single_page_object in page_objects_list:
                if single_page_object.values_where_changed_after_test:
                    single_page_object.clean_after_test()
                    time.sleep(3)

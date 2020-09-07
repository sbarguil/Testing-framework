import pytest


class BaseTest:
    @pytest.fixture
    def create_page_object(self, create_page_object_arg):
        test_case_file = create_page_object_arg['test_case_file']
        test_case_name = create_page_object_arg['test_case_name']
        page_object_class = create_page_object_arg['page_object_class']
        test_page_object = page_object_class(test_case_file=test_case_file, test_case_name=test_case_name)
        yield test_page_object
        if test_page_object.values_where_changed_after_test:
            test_page_object.clean_after_test()

    @pytest.fixture
    def multiple_create_page_objects(self, multiple_create_page_objects_arg):
        page_objects_list = []
        rpc_index = 0
        for single_page_object_class in multiple_create_page_objects_arg['page_object_rpcs_classes']:
            test_page_object = single_page_object_class(test_case_file=multiple_create_page_objects_arg['test_case_file'],
                                                        test_case_name=multiple_create_page_objects_arg['test_case_name'],
                                                        rpc_idx=rpc_index)
            page_objects_list.append(test_page_object)
            rpc_index = rpc_index + 1

        yield page_objects_list

        if multiple_create_page_objects_arg['rpc_clean_order']:
            for rpc_clean_index in multiple_create_page_objects_arg['rpc_clean_order']:
                if page_objects_list[rpc_clean_index].values_where_changed_after_test:
                    page_objects_list[rpc_clean_index].clean_after_test()
        else:
            for single_page_object in page_objects_list:
                if single_page_object.values_where_changed_after_test:
                    single_page_object.clean_after_test()

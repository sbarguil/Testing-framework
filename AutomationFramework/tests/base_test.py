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

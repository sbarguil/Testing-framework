import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("tests_sub_set", help="The sub set of tests to execute. It can be a block or a sub-block. i.e. "
                                              "tests/hardware, tests/hardware/test_hw_component.py or "
                                              "tests/hardware/test_hw_component.py::TestHardwareComponent::test_hw_component_description")
    args = parser.parse_args()

    sub_set = args.tests_sub_set
    print(sub_set)

    # Delete cumulative logs file
    excel_logs_path = os.path.dirname(os.path.realpath(__file__)) + '/excel_logs/'
    cumulative_logs_path = excel_logs_path + 'cumulative_log.xlsx'
    print('Removing file: ' + cumulative_logs_path)

    try:
        os.remove(cumulative_logs_path)
    except FileNotFoundError:
        print('File cummulative_logs.xlxs not found for delete')

    # Run pytest
    split_sub_set = sub_set.split('/')

    try:
        while True:
            split_sub_set.remove('')
    except:
        print('Split sub-set clean')

    if len(split_sub_set) == 2:
        output_file_name = split_sub_set[-1]
    elif len(split_sub_set) == 3:
        output_file_name = split_sub_set[-2] + '_' + split_sub_set[-1].split('.')[0]
        last_item_split = split_sub_set[2].split('::')
        if len(last_item_split) > 1:
            output_file_name = output_file_name + '_' + last_item_split[-1]
    else:
        raise Exception('Not allowed sub set. Expected notation: tests/hardware, tests/hardware/test_hw_component.py '
                        'or tests/hardware/test_hw_component.py::TestHardwareComponent::test_hw_component_description')

    pytest_command = 'py.test ' + sub_set + ' --excelreport=reports/' + output_file_name + '_report.xls'

    print('- Running ' + pytest_command)
    os.system(pytest_command)

    # Change the cumulative log file name to sub_set file log
    print('- Rename cummulative_logs.xlxs')
    os.rename(cumulative_logs_path, excel_logs_path + output_file_name + '_logs.xlsx')

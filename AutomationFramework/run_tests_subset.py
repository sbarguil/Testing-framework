#/usr/bin/python

import argparse
import sys
import os

print(sys.argv)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("output_format", help="The format of the output. i.e. excel")
    parser.add_argument("tests_subset_location", help="This can be either a file location (tests/hardware/test_hw_cpu.py) "
                                                      "or a folder path (tests/hardware/).")

    args = parser.parse_args()

    print(args.output_format)
    print(args.tests_subset_location)

    os.system('ls -l')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    # Tiene que revisar si hay un archivo que se llama como el que le toca a la ejecucion, si si está borrelo
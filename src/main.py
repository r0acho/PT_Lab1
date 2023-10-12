# -*- coding: utf-8 -*-
import argparse
import sys

from StudentAnalyzer import StudentAnalyzer
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = XmlDataReader()
    students = reader.read(path)
    print("Students: ", students)
    first_quartile_students = StudentAnalyzer().\
        students_in_first_quartile(students)
    print("Students at first quartile : ", first_quartile_students)


if __name__ == "__main__":
    main()

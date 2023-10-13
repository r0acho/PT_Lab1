# -*- coding: utf-8 -*-
import argparse
import sys
from DataReader import DataReader
import os

from StudentAnalyzer import StudentAnalyzer
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def get_current_reader(path: str) -> DataReader:
    _, file_extension = os.path.\
        splitext(path)
    match file_extension:
        case ".txt":
            return TextDataReader()
        case ".xml":
            return XmlDataReader()
        case _:
            raise ValueError("Неподдерживаемый формат")


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = get_current_reader(path)
    students = reader.read(path)
    print("Students: ", students)
    first_quartile_students = StudentAnalyzer().\
        students_in_first_quartile(students)
    print("Students at first quartile : ", first_quartile_students)


if __name__ == "__main__":
    main()

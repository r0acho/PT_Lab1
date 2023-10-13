# -*- coding: utf-8 -*-
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader
from src.main import get_path_from_arguments, get_current_reader
import pytest


@pytest.fixture()
def correct_arguments_string_txt() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.txt"], "/home/user/file.txt"

@pytest.fixture()
def correct_arguments_string_xml() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.txt"], "/home/user/file.xml"

@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"]


def test_get_path_from_correct_arguments(
        correct_arguments_string_txt: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string_txt[0])
    assert path == correct_arguments_string_txt[1]


def test_get_path_from_noncorrect_arguments(
        noncorrect_arguments_string: list[str]) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string[0])

    assert e.type == SystemExit

def get_correct_reader_txt(
        correct_arguments_string_txt: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string_txt[0])
    assert TextDataReader == get_current_reader(path)

def get_correct_reader_xml(
        correct_arguments_string_xml: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string_xml[0])
    assert XmlDataReader == get_current_reader(path)

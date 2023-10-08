import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        xml = """<?xml version="1.0" encoding="UTF-8" ?>
                <root>
                    <Иванов_Иван_Иванович>
                        <математика>67</математика>
                        <литература>100</литература>
                        <программирование>91</программирование>
                    </Иванов_Иван_Иванович>
                    <Петров_Петр_Петрович>
                        <математика>78</математика>
                        <химия>87</химия>
                        <социология>61</социология>
                    </Петров_Петр_Петрович>
                </root>"""
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return xml, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        xml_content = XmlDataReader().read(filepath_and_data[0])
        assert xml_content == filepath_and_data[1]

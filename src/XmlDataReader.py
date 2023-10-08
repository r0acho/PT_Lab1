import xml.etree.ElementTree as ElementTree
from Types import DataType
from DataReader import DataReader


class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ElementTree.parse(path)
        root = tree.getroot()

        for student_elem in root:
            student_name = student_elem.tag
            scores = []
            for subject_elem in student_elem:
                subject = subject_elem.tag
                score = int(subject_elem.text)
                scores.append((subject, score))
            self.students[student_name] = scores

        return self.students

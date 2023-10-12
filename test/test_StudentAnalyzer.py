import pytest
from src.StudentAnalyzer import StudentAnalyzer


class TestStudentAnalyzer:
    @pytest.fixture()
    def test_data(self):
        return {
            "Иванов": [("математика", 91), ("химия", 100)],
            "Петров": [("русский язык", 87), ("литература", 78)],
            "Сидоров": [("география", 60), ("физика", 75)],
        }

    def test_students_in_first_quartile(self, test_data):
        analyzer = StudentAnalyzer()
        expected_students = {
            "Сидоров": [("география", 60), ("физика", 75)],
        }

        students_in_quartile = analyzer.students_in_first_quartile(test_data)
        assert students_in_quartile == expected_students

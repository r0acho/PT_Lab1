from typing import List, Dict, Tuple
from Types import DataType


class StudentAnalyzer:
    def _calculate_quartiles(self, data: DataType) -> List[int]:
        # Соберем все рейтинги в один список
        all_ratings = [score for student_scores in data.values()
                       for _, score in student_scores]

        # Отсортируем рейтинги по возрастанию
        sorted_ratings = sorted(all_ratings)

        # Разделим рейтинги на 4 части (квартили)
        quartile1_index = len(sorted_ratings) // 4
        quartile2_index = len(sorted_ratings) // 2
        quartile3_index = (3 * len(sorted_ratings)) // 4

        # Найдем значения квартилей
        quartile1 = sorted_ratings[quartile1_index]
        quartile2 = sorted_ratings[quartile2_index]
        quartile3 = sorted_ratings[quartile3_index]

        return [quartile1, quartile2, quartile3]

    def students_in_first_quartile(self, data: DataType) -> \
            Dict[str, List[Tuple[str, int]]]:
        quartiles = self._calculate_quartiles(data)
        quartile1 = quartiles[0]

        students_in_quartile = {}
        for student, scores in data.items():
            student_average = sum(score for _, score in scores) / len(scores)
            if student_average <= quartile1:
                students_in_quartile[student] = scores

        return students_in_quartile

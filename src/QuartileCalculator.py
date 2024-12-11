# -*- coding: utf-8 -*-
from typing import List, Dict


class QuartileCalculator:

    @staticmethod
    def calculate_quartiles(ratings: List[float]) -> Dict[str, float]:
        """
        Рассчитывает квартили (Q1, Q2, Q3) на основе списка рейтингов.
        :param ratings: Список рейтингов студентов.
        :return: Словарь с квартилями {Q1, Q2, Q3}.
        """
        sorted_ratings = sorted(ratings)
        n = len(sorted_ratings)

        if n == 0:
            return {"Q1": 0, "Q2": 0, "Q3": 0}
        elif n == 1:
            return {"Q1": sorted_ratings[0],
                    "Q2": sorted_ratings[0],
                    "Q3": sorted_ratings[0]}
        elif n == 2:
            return {
                "Q1": sorted_ratings[0],
                "Q2": (sorted_ratings[0] + sorted_ratings[1]) / 2,
                "Q3": sorted_ratings[1]
            }

        # Функция для расчета квартиля
        def get_quartile(q: float) -> float:
            index = q * (n - 1)
            lower = sorted_ratings[int(index)]
            upper = (
                sorted_ratings[int(index) + 1]
                if int(index) + 1 < n
                else lower
            )
            return lower + (index - int(index)) * (upper - lower)

        # Расчет Q1, Q2, Q3
        q1 = get_quartile(0.25)
        q2 = get_quartile(0.5)
        q3 = get_quartile(0.75)

        return {
            "Q1": q1,
            "Q2": q2,
            "Q3": q3
        }

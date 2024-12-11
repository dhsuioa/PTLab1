# -*- coding: utf-8 -*-
import pytest
from src.QuartileCalculator import QuartileCalculator


class TestQuartileCalculator:

    @pytest.fixture()
    def ratings_data(self) -> list[float]:
        return [60, 70, 80, 90, 100]

    def test_calculate_quartiles(self, ratings_data: list[float]) -> None:
        quartiles = QuartileCalculator.calculate_quartiles(ratings_data)
        assert quartiles["Q1"] == 70
        assert quartiles["Q2"] == 80
        assert quartiles["Q3"] == 90

    def test_calculate_quartiles_with_one_element(self) -> None:
        ratings_data = [50]
        quartiles = QuartileCalculator.calculate_quartiles(ratings_data)
        assert quartiles["Q1"] == 50
        assert quartiles["Q2"] == 50
        assert quartiles["Q3"] == 50

    def test_calculate_quartiles_with_two_elements(self) -> None:
        ratings_data = [50, 100]
        quartiles = QuartileCalculator.calculate_quartiles(ratings_data)
        assert quartiles["Q1"] == 50
        assert quartiles["Q2"] == 75
        assert quartiles["Q3"] == 100

    def test_calculate_quartiles_with_empty_list(self) -> None:
        ratings_data = []
        quartiles = QuartileCalculator.calculate_quartiles(ratings_data)
        assert quartiles["Q1"] == 0
        assert quartiles["Q2"] == 0
        assert quartiles["Q3"] == 0

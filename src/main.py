# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from QuartileCalculator import QuartileCalculator


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)

    # Рассчитываем рейтинг для всех студентов
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    # Получаем список рейтингов
    ratings_list = list(rating.values())

    # Рассчитываем квартили
    quartiles = QuartileCalculator.calculate_quartiles(ratings_list)
    print("Quartiles: ", quartiles)

    # Выводим студентов из третьей квартили
    q3 = quartiles["Q3"]
    print(f"Students in the 3rd quartile (rating >= {q3}):")
    for student, score in rating.items():
        if score >= q3:
            print(f"{student}: {score}")


if __name__ == "__main__":
    main()

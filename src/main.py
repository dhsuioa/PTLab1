# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from JsonDataReader import JsonDataReader
from QuartileCalculator import QuartileCalculator


def get_path_from_arguments(args) -> tuple:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p",
                        dest="path",
                        type=str,
                        required=True,
                        help="Path to datafile")
    parser.add_argument("-f",
                        dest="format",
                        type=str,
                        required=True,
                        choices=["txt", "json"],
                        help="Format of the datafile")
    args = parser.parse_args(args)
    return args.path, args.format


def main():
    path, file_format = get_path_from_arguments(sys.argv[1:])

    # Выбор читателя данных в зависимости от формата файла
    if file_format == "txt":
        reader = TextDataReader()
    elif file_format == "json":
        reader = JsonDataReader()
    else:
        raise ValueError("Unsupported file format")

    # Чтение данных
    students = reader.read(path)
    print("Students: ", students)

    # Расчет рейтинга для всех студентов
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    # Получаем список рейтингов
    ratings_list = list(rating.values())

    # Расчет квартилей
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

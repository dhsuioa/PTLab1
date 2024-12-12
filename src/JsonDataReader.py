# -*- coding: utf-8 -*-
import json
from Types import DataType
from DataReader import DataReader


class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        """
        Читает данные из JSON-файла и возвращает словарь студентов.
        :param path: Путь к JSON-файлу.
        :return: Словарь студентов.
        """
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
            for student, subjects in data.items():
                self.students[student] = []
                for subject, score in subjects.items():
                    self.students[student].append((subject, int(score)))
        return self.students

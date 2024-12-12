# Лабораторная 1 по дисциплине "Технологии программирования"

## Описание проекта

Проект рассчитывает средний рейтинг студентов по дисциплинам. Данные о студентах и их оценках хранятся в текстовом файле. Проект написан на языке Python 3, модульное тестирование осуществляется с помощью библиотеки pytest.

## Структура проекта

- `github/workflows/github-actions-testing.yml`: Файл для настройки GitHub Actions.
- `data/data.txt`: Файл с данными о студентах и их оценках.
- `src/`: Исходный код проекта.
- `test/`: Модульные тесты.
- `requirements.txt`: Зависимости проекта.

## UML-диаграмма

```mermaid
classDiagram
    class CalcRating {
        - data: DataType
        - rating: RatingType
        + __init__(data: DataType)
        + calc() -> RatingType
    }

    class DataReader {
        <<abstract>>
        + read(path: str) -> DataType
    }

    class TextDataReader {
        - key: str
        - students: DataType
        + read(path: str) -> DataType
    }

    class QuartileCalculator {
        + calculate_quartiles(ratings: List[float]) -> Dict[str, float]
    }

    class main {
        + get_path_from_arguments(args) -> str
        + main()
    }

    DataReader <|-- TextDataReader : Наследует
    CalcRating --> DataReader : Использует
    main --> CalcRating : Использует
    main --> TextDataReader : Использует
    main --> QuartileCalculator : Использует

import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_python_less_salary() -> Vacancy:
    return Vacancy(
        name="Python dev (less)", link="python.test", salary={"from": 1000, "to": 2000}, description="Test description"
    )


@pytest.fixture
def vacancy_python_large_salary() -> Vacancy:
    return Vacancy(
        name="Python dev (large)",
        link="python.test",
        salary={"from": 100000, "to": 200000},
        description="Test description",
    )


@pytest.fixture
def vacancy_python() -> Vacancy:
    return Vacancy(
        name="Python", link="python.test", salary={"from": 10000, "to": 20000}, description="Test description"
    )


def vacancy_python_without_salary() -> Vacancy:
    return Vacancy(name="Python dev", link="python.test", salary=None, description="Test description")


@pytest.fixture
def list_of_vacancies_dict() -> list[dict]:
    return [
        {
            "name": "Python-разработчик",
            "link": "https://hh.ru/vacancy/125138836",
            "salary": {"from": 500000, "to": 0},
            "description": "Опыт коммерческой разработки на <highlighttext>Python</highlighttext> 3.9+. "
                           "Отличные знания FastAPI (или аналогов: Django REST Framework, Flask). "
                           "Уверенные навыки работы...",
        },
        {
            "name": "Python Django developer",
            "link": "https://hh.ru/vacancy/125010047",
            "salary": {"from": 0, "to": 1000},
            "description": "Опыт: 3–6 лет в разработке на <highlighttext>Python</highlighttext>/Django. "
                           "Multi tenancy. "
                           "Уверенное владение <highlighttext>Python</highlighttext> 3 и фреймворком Django (DRF). ",
        },
        {
            "name": "Директор по финансовому моделированию и сценарному анализу",
            "link": "https://hh.ru/vacancy/125169109",
            "salary": {"from": 0, "to": 0},
            "description": "Навыки анализа данных с помощью <highlighttext>Python</highlighttext> и R. "
                           "Опыт работы с СУБД PostgreSQL и SQLite. Знание подходов к оценке кредитных...",
        },
        {
            "name": "Тестировщик ПО",
            "link": "https://hh.ru/vacancy/125165964",
            "salary": {"from": 0, "to": 0},
            "description": "Опыт работы с SQL для проверки данных в базах. Знание основ программирования (например, "
                           "<highlighttext>Python</highlighttext>, С/С++) будет плюсом. ",
        },
    ]


@pytest.fixture
def vacancies_list() -> list[Vacancy]:
    list_vacancies_dicts = [
        {
            "name": "Python-разработчик",
            "link": "https://hh.ru/vacancy/125138836",
            "salary": {"from": 500000, "to": 0},
            "description": "Опыт коммерческой разработки на <highlighttext>Python</highlighttext> 3.9+. "
                           "Отличные знания FastAPI (или аналогов: Django REST Framework, Flask). "
                           "Уверенные навыки работы...",
        },
        {
            "name": "Python Django developer",
            "link": "https://hh.ru/vacancy/125010047",
            "salary": {"from": 0, "to": 1000},
            "description": "Опыт: 3–6 лет в разработке на <highlighttext>Python</highlighttext>/Django. "
                           "Multi tenancy. "
                           "Уверенное владение <highlighttext>Python</highlighttext> 3 и фреймворком Django (DRF). ",
        },
        {
            "name": "Директор по финансовому моделированию и сценарному анализу",
            "link": "https://hh.ru/vacancy/125169109",
            "salary": {"from": 0, "to": 0},
            "description": "Навыки анализа данных с помощью <highlighttext>Python</highlighttext> и R. "
                           "Опыт работы с СУБД PostgreSQL и SQLite. Знание подходов к оценке кредитных...",
        },
        {
            "name": "Тестировщик ПО",
            "link": "https://hh.ru/vacancy/125165964",
            "salary": {"from": 0, "to": 0},
            "description": "Опыт работы с SQL для проверки данных в базах. Знание основ программирования (например, "
                           "<highlighttext>Python</highlighttext>, С/С++) будет плюсом. ",
        },
    ]

    return [Vacancy.new_vacancy(vacancy) for vacancy in list_vacancies_dicts]


@pytest.fixture
def vacancies_list_two_vac() -> list[Vacancy]:
    list_vacancies_dicts = [
        {
            "name": "Python-разработчик",
            "link": "https://hh.ru/vacancy/125138836",
            "salary": {"from": 500000, "to": 0},
            "description": "Опыт коммерческой разработки на <highlighttext>Python</highlighttext> 3.9+. "
                           "Отличные знания FastAPI (или аналогов: Django REST Framework, Flask). "
                           "Уверенные навыки работы...",
        },
        {
            "name": "Python Django",
            "link": "https://hh.ru/vacancy/",
            "salary": {"from": 10000, "to": 100000},
            "description": "Опыт: 6 лет в разработке на Python",
        },
    ]

    return [Vacancy.new_vacancy(vacancy) for vacancy in list_vacancies_dicts]


@pytest.fixture
def area_api_request() -> list:
    return [
        {
            "id": "113",
            "parent_id": None,
            "name": "Россия",
            "areas": [
                {
                    "id": "1620",
                    "parent_id": "113",
                    "name": "Республика Марий Эл",
                    "areas": [
                        {"id": "4228", "parent_id": "1620", "name": "Виловатово", "areas": [], "utc_offset": "+03:00"},
                        {"id": "1621", "parent_id": "1620", "name": "Волжск", "areas": [], "utc_offset": "+03:00"},
                        {"id": "1622", "parent_id": "1620", "name": "Звенигово", "areas": [], "utc_offset": "+03:00"},
                    ],
                }
            ],
        }
    ]

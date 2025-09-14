import os

from src.file_handler import VacancyJSONHandler
from src.vacancy import Vacancy


def test_vacancy_json_handler(vacancies_list: list[Vacancy], vacancies_list_two_vac: list[Vacancy]) -> None:
    json_handler = VacancyJSONHandler("test.json")

    # Test for save list of vacancies in file
    json_handler.save_vacancies(vacancies_list)

    list_of_save_vacancies = json_handler.get_vacancies()

    assert len(list_of_save_vacancies) == 4

    # Test for add list of vacancies in file (one of two vacancies is existed in file)

    json_handler.save_vacancies(vacancies_list_two_vac)

    list_of_save_vacancies = json_handler.get_vacancies()

    assert len(list_of_save_vacancies) == 5

    # delite and assert vacancies in file
    json_handler.del_vacancies([1, 0])

    list_of_save_vacancies = json_handler.get_vacancies()

    assert len(list_of_save_vacancies) == 3

    # Delite test file from data/
    try:
        os.remove("data/test.json")
    except FileNotFoundError:
        pass


#
# def test_vacancy_csv_handler(vacancies_list):
#     # create new csv handler object
#     json_handler = VacancyJSONHandler("test.csv")
#
#     try:
#         os.remove("data/csv.json")
#     except FileNotFoundError:
#         pass

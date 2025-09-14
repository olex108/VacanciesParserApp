from src.file_handler import VacancyJSONHandler
from src.vacancy import Vacancy
from src.selection import select_file, select_request_params, select_salary_sort_params, select_del_elements


def work_with_vacancies(vacancies_list: list[Vacancy], file_name: str = None) -> None:
    """
    Function for selection operation with vacation lists from file or hh.ru request
    1 - Call function for selection sort functions
    2 - Save vacation list in file
    3 - Delite vacations fron list or file

    :param vacancies_list: list of vacancies
    :param file_name: name of file
    """

    [print(f"{index} - {vacancy}") for index, vacancy in enumerate(vacancies_list)]

    print("1. Отсортировать вакансии\n"
          "2. Сохранить вакансии\n"
          "3. Удалить вакансии\n"
          "4. Вернуться в стартовое меню\n")

    user_step = input("Действие:")

    if user_step == "1":
        # For sort vacations we use class SortVacation and get result of sorting to call back function
        # work_with_file_vacancies
        vacancies_list = select_salary_sort_params(vacancies_list)
        work_with_vacancies(vacancies_list, file_name)

    elif user_step == "2":
        select_file_name = select_file()
        if select_file_name is None:
            select_file_name = input("Введите название файла:")
        file = VacancyJSONHandler(select_file_name)
        file.save_vacancies(vacancies_list)
        main_menu()

    elif user_step == "3":
        del_elements_list = select_del_elements()
        if file_name:
            file_handler = VacancyJSONHandler(file_name)
            file_handler.del_vacancies(del_elements_list)
            vacancies_list = file_handler.get_vacancies()
            print(f"Открыт файл: {file_name}")
            work_with_vacancies(vacancies_list, file_name)
        else:

            for index in sorted(del_elements_list, reverse=True):
                del vacancies_list[index]
            work_with_vacancies(vacancies_list, file_name)

    elif user_step == "4":
        main_menu()

    else:
        print("Ошибка ввода")
        work_with_vacancies(vacancies_list, file_name)


def main_menu():
    """
    Function start work of user, select operation with files or hh.ru
    """

    print("Программа для работы с вакансиями\n")
    print("1. Просмотр файлов по сохраненным вакансиям\n"
          "2. Получение новых данных из сайта hh.ru")

    user_step = input("Действие:")
    if user_step == "1":

        # call select_file() if file not exist return to user_interaction()
        file_name = select_file()
        if file_name:
            file_handler = VacancyJSONHandler(file_name)
            vacancies_list = file_handler.get_vacancies()
            print(f"Открыт файл: {file_name}")
            work_with_vacancies(vacancies_list, file_name)
        else:
            main_menu()
    elif user_step == "2":
        vacancies_list = select_request_params()
        work_with_vacancies(vacancies_list)
    else:
        print("Ошибка ввода")
        main_menu()


if __name__ == "__main__":
    main_menu()

import os

from src.external_api import HeadHunterApiService
from src.vacancy import Vacancy


def select_file() -> str | None:
    """
    Function to select file in data/ return select file name or None if there are no file in data/
    :return: name of file
    """

    files = os.listdir("data")
    if len(files) > 0:
        print("Список файлов" "0 - Создать новый файл")
        [print(f"{index + 1} - {file}") for index, file in enumerate(files)]
        user_step = input("Выберите файл:")
        if user_step == "0":
            return None
        try:
            return files[int(user_step) - 1]
        except IndexError:
            print("Неправильный номер файла")
            return None
        except ValueError:
            print("Неправильный номер файла")
            return None
    else:
        print("У Вас нет сохраненных файлов")
        return None


def select_request_params() -> list[Vacancy]:
    """
    Function to get user vacations params and call get_vacancies method of HeadHunterApiService

    :return: vacation list
    """

    print("Введите параметры для поиска вакансий:")
    search_area_name = input("Локация(не обязательно):")
    search_word = input("Ключевое слово:")
    vacancies_count = int(input("Количество(не обязательно):"))

    vacation_request = HeadHunterApiService()

    return vacation_request.get_vacancies(search_word, search_area_name, vacancies_count)


def select_salary_sort_params(vacancies_list: list[Vacancy]) -> list[Vacancy] | None:
    """
    Function for select sort parameter
    Function ask user method of sort vacancies list.
    If user get sort by salary range, call function get_vacations_by_salary()
    :param vacancies_list: list of vacancies
    :return: sorted vacancies_list
    """

    print(
        "1. Отсортировать вакансии по зарплате (по возрастанию)\n"
        "2. Отсортировать вакансии по зарплате (по убыванию)\n"
        "3. Выбрать диапазон зарплат"
    )

    user_step = input("Действие:")

    if user_step == "1":
        return sort_vacations_by_salary(vacancies_list, True)
    elif user_step == "2":
        return sort_vacations_by_salary(vacancies_list, False)
    elif user_step == "3":
        return filter_vacations_by_salary(vacancies_list)
    else:
        print("Ошибка ввода")
        return vacancies_list


def sort_vacations_by_salary(vacancies_list: list[Vacancy], reverse_param: bool) -> list[Vacancy]:
    """
    Function for sort vacancies by salary
    :param vacancies_list: list of vacations
    :param reverse_param: bool parameter of sorting.
    :return: sorted vacation list
    """
    return sorted(vacancies_list, reverse=reverse_param)


def filter_vacations_by_salary(vacancies_list: list[Vacancy]) -> list[Vacancy] | None:
    """
    Function for sort vacancies by salary range
    Function ask user salary range.

    :param vacancies_list: list of vacancies
    :return: sorted vacancies_list
    """

    salary_range = input("Введите диапазон зарплат через (-) без пробелов:")
    try:
        return [
            vacation
            for vacation in vacancies_list
            if int(salary_range.split("-")[0]) <= vacation <= int(salary_range.split("-")[1])
        ]
    except IndexError:
        print("Ошибка ввода")
        return vacancies_list
    except TypeError:
        print("Ошибка ввода")
        return vacancies_list


def select_del_elements() -> list[int]:
    """
    Function for select indexes of vacations to del

    :return: sorted list of indexes
    """

    print(
        "Для удаления по индексам элементов пропишите индексы через запятую(без пробела)\n"
        "Для удаления интервала элементов пропишите индексы начала и конца через дефис(-)"
    )

    user_step = input("Действие:")

    if "-" in user_step:
        try:
            return sorted(
                [num for num in range(int(user_step.split("-")[0]), int(user_step.split("-")[1]) + 1)], reverse=True
            )
        except ValueError:
            print("Ошибка ввода")
            return []
    elif "," in user_step:
        try:
            return sorted([int(num) for num in user_step.split(",")], reverse=True)
        except ValueError:
            print("Ошибка ввода")
            return []
    else:
        print("Ошибка ввода")
        return []

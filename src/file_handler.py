import json
import os
from abc import ABC, abstractmethod
from typing import Any

from src.vacancy import Vacancy


class VacancyFileHandler(ABC):
    """
    Abstract class for work with files, include save, get or del vacations from files
    """

    @abstractmethod
    def save_vacancies(self, save_data: list[Vacancy]) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> list:
        pass

    @abstractmethod
    def del_vacancies(self, list_of_index: list[int]) -> None:
        pass


class VacancyCSVHandler(VacancyFileHandler):
    """
    Class for work with CSV files, include save, get or del vacations.
    """

    file_name: str

    def __init__(self, file_name: str = "vacancies.csv") -> None:
        self.__file_name = file_name
        self.__path_to_file = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "data", self.__file_name)

    def save_vacancies(self, save_data: list[Vacancy]) -> None:

        pass

    @abstractmethod
    def get_vacancies(self) -> list:

        pass

    def del_vacancies(self, *args: list[int]) -> None:

        pass


class VacancyJSONHandler(VacancyFileHandler):
    """
    Class for work with JSON files, with include save, get or del vacancy.
    """

    file_name: str

    def __init__(self, file_name: str = "vacancies.json"):
        self.__file_name = file_name
        self.__path_to_file = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "data", self.__file_name)

    def __verification_data(self, add_data: list[dict]) -> list[dict] | Any:
        """
        Method of verification vacancies(dictionary) data, if vacancy exist new vacancy will be not add.
        """

        try:
            with open(self.__path_to_file, "r", encoding="utf-8") as file:
                file_data = json.load(file)

            for vacancy in add_data:
                if vacancy not in [voc for voc in file_data]:
                    file_data.append(vacancy)

            return file_data

        except FileNotFoundError:
            return add_data

    def save_vacancies(self, save_data: list[Vacancy]) -> None:
        """
        Method to save vacancies in JSON file.
        For add vacancies in file with vacancies, call method __verification_data

        :param save_data: list of vacancies
        """

        save_data_dicts = self.__verification_data([vacancy.get_dict() for vacancy in save_data])

        with open(self.__path_to_file, "w", encoding="utf-8") as file:
            json.dump(save_data_dicts, file, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> list[Vacancy] | list:
        """
        Method to get vacancies from JSON file

        :return data_json: list of vacancies from json
        """

        try:
            with open(self.__path_to_file, "r", encoding="utf-8") as file:
                data_json = json.load(file)
                vacancies_list = [Vacancy.new_vacancy(vacancy) for vacancy in data_json]
            return vacancies_list
        except FileNotFoundError:
            print("Файл не найден")
            return []

    def del_vacancies(self, list_of_index: list[int]) -> None:
        """
        Method to del vacancies from JSON file by indexes

        :param list_of_index: list of indexes for del from file
        """

        try:
            with open(self.__path_to_file, "r", encoding="utf-8") as file:
                file_data = json.load(file)

            for index in list_of_index:
                del file_data[index]

            with open(self.__path_to_file, "w", encoding="utf-8") as file:
                json.dump(file_data, file, ensure_ascii=False, indent=4)

        except IndexError:
            print("Индекс выходит за рамки списка")

        except FileNotFoundError:
            print("Файл не найден")

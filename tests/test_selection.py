from typing import Any
from unittest.mock import patch

from src.selection import filter_vacations_by_salary, select_del_elements, select_file, sort_vacations_by_salary
from src.vacancy import Vacancy


def test_select_file() -> None:
    with patch("os.listdir") as mock_files_list:

        mock_files_list.return_value = []
        assert select_file() is None

        mock_files_list.return_value = ["test_1.test", "test_2.test"]

        with patch("builtins.input") as mock_input:

            mock_input.return_value = "0"
            assert select_file() is None

            mock_input.return_value = "1"
            assert select_file() == "test_1.test"

            mock_input.return_value = "3"
            assert select_file() is None

            mock_input.return_value = "word"
            assert select_file() is None


def test_sort_vacations_by_salary(vacancy_python_large_salary: Vacancy, vacancy_python_less_salary: Vacancy) -> None:
    list_of_vacancies = [vacancy_python_less_salary, vacancy_python_large_salary]
    sorted_list = sort_vacations_by_salary(list_of_vacancies, reverse_param=True)
    assert sorted_list[0] == vacancy_python_large_salary
    assert sorted_list[1] == vacancy_python_less_salary

    sorted_list = sort_vacations_by_salary(list_of_vacancies, reverse_param=False)
    assert sorted_list[1] == vacancy_python_large_salary
    assert sorted_list[0] == vacancy_python_less_salary


def test_filter_vacations_by_salary(
    capsys: Any, vacancy_python_large_salary: Vacancy, vacancy_python_less_salary: Vacancy
) -> None:
    list_of_vacancies = [vacancy_python_less_salary, vacancy_python_large_salary]

    with patch("builtins.input") as mock_input:
        mock_input.return_value = "30000-400000"

        filtered_list = filter_vacations_by_salary(list_of_vacancies)

        assert len(filtered_list) == 1

        mock_input.return_value = "30000"
        filter_vacations_by_salary(list_of_vacancies)

        capture = capsys.readouterr()
        result = capture.out
        assert result == "Ошибка ввода\n"

        mock_input.return_value = "30000"
        filter_vacations_by_salary(list_of_vacancies)
        assert filter_vacations_by_salary(list_of_vacancies) == list_of_vacancies


def test_select_del_elements(capsys: Any) -> None:
    with patch("builtins.input") as mock_input:
        # Test for correct inputs
        mock_input.return_value = "1-3"
        assert select_del_elements() == [3, 2, 1]

        mock_input.return_value = "1,2,3"
        assert select_del_elements() == [3, 2, 1]

        # Test for incorrect inputs
        mock_input.return_value = "30000"
        assert select_del_elements() == []

        mock_input.return_value = "word, word"
        assert select_del_elements() == []

        mock_input.return_value = "word-word"
        assert select_del_elements() == []

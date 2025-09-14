# VacanciesParserApp

# E-store Template

## Table of Contents
- [Installation]
- [Description of Functionality]
- [Testing]

## Installation:

```
git clone https://github.com/olex108/VacanciesParserApp.git
```

## Description of Functionality:

### Main:

main_menu(): Function start work of user, select operation with files or hh.ru

work_with_vacancies(): Function for selection operation with vacation lists from file or hh.ru request
    1 - Call function for selection sort functions
    2 - Save vacation list in file
    3 - Delite vacations fron list or file

### Functions:

select_file(): Function to select file in data/ return select file name or None if there are no file in data/

select_request_params(): Function to get user vacations params and call get_vacancies method of HeadHunterApiService

select_salary_sort_params(): Function for select sort parameter
Function ask user method of sort vacancies list.
If user get sort by salary range, call function get_vacations_by_salary()

select_del_elements(): Function for select indexes of vacations to del


### Classes:

#### Abstract Classes

1. BaseApiService - Abstract class to work with API

_get_api_response: Method to connection and get response by API

get_vacancies: Method to get vacancies by search parameters

2. VacancyFileHandler - Abstract class for work with files, include save, get or del vacations from files

save_vacancies: Method to save vacancies in file

get_vacancies: Method to get list of vacancies from file

del_vacancies: Method to del list of indexes of vacancies from file

#### Vacancy

Class for work with vacancy.
In class described dander methods for print and compare vacancies, add new vacancy and validation of salary

```commandline
name: Name of the vacancy
link: Link on hh.ru
salary: Dict of salary "from" "to"
description: Description of the vacancy
```

#### HeadHunterApiService 

Class for work with site hh.ru

```commandline
vacancies: list of vacation
```

__get_area_id: Method for search area id from Api HeadHunter request by area name. Ger response from method _get_api_response by url: "https://api.hh.ru/areas". If response status code valid start recurs search in lists of data with function recurs_search_by_name()

_get_api_response: Method for connection to HeadHunter API

get_vacancies: Method to get vacancies by search parameters. Method call method _get_api_response to get vacancies data


#### VacancyJSONHandler

Class for work with JSON files, with include save, get or del vacancy.

```commandline
file_name: Name of file wiht vacancies data
path_to_file: path to file
```

__verification_data: Method of verification vacancies(dictionary) data, if vacancy exist new vacancy will be not add.

save_vacancies: Method to save vacancies in JSON file. For add vacancies in file with vacancies, call method __verification_data

get_vacancies: Method to get vacancies from JSON file

del_vacancies: Method to del vacancies from JSON file by indexes


##### VacancyCSVHandler

Class for work with CSV files, include save, get or del vacations.
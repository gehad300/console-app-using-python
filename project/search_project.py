import re


def search_project():
    date_regex = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
    print("please write start and end date to search")
    search_start_date = input("please enter start date:")
    search_end_date = input("please enter end date:")
    while not re.search(date_regex, search_start_date) and re.search(date_regex, search_end_date):
        search_start_date = input("please enter valid start date:")
        search_end_date = input("please enter valid end date:")

    file = open("project_data.txt", 'r')
    for data in file:
        data_splitted = data.split(":")
        if data_splitted[3] == search_start_date and data_splitted[4] == search_end_date:
            print("========================")
            return data

    return None

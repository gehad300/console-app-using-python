import re


def create_project(email):
    date_regex = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'

    Title = input("please enter a project Title: ")
    file = open("project_data.txt", 'r')
    for data in file:
        data_validation = data.split(":")
        while data_validation[0] == Title:
            print("this Title is already exists:")
            print("=================================")
            Title = input("please enter a valid Title:")
            print("=================================")
    while not Title.isalnum():
        Title = input("please enter a valid Title: ")
    details = input("please enter some details about project : \n")

    total_target = input("please enter total target:")
    while total_target.isalpha():
        total_target = input("please enter numeric total target: ")
    start_date = input("please enter start date for the project: ")
    while not re.search(date_regex, start_date):
        start_date = input("please enter start date:")
    end_date = input("please enter end date:")
    while not re.search(date_regex, end_date):
        end_date = input("please enter an end date:")

    create = open("project_data.txt", 'a')
    create.write(Title+':'+details+':'+total_target+':' +
                 start_date+':'+end_date+':'+email + '\n')
    create.close()

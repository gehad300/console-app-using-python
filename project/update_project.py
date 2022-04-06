import re
def update_project(email):
    new_list = []
    date_regex = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
    old_Title = input("please Enter project title: ")
    while not old_Title.isalnum():
        old_Title = input("please Enter project title: ")
    
    try:
        data_updated = open('project_data.txt', 'r')
        for data in data_updated:
            data_splitted = data.split(':')
            mail = data_splitted[5]
            email1 = email+'\n'
            if email1 == data_splitted[5] and old_Title == data_splitted[0]:
                print("Change yout old Title : ", data_splitted[0], "To")
                new_Title = input()
                while not new_Title.isalnum():
                    print("please enter a valid title:")
                    new_Title = input()

                print("Change yout old Details : ", data_splitted[1], "To")
                new_Details = input()
                while not new_Details.isalnum():
                    print("please enter a valid Details:")
                    new_Details = input()
                print("Change your Total target : ", data_splitted[2], "To")
                new_total_target = input()
                while not new_total_target.isnumeric():
                    print("please enter a numeric target:")
                    new_total_target = input()
                print("Change yout old Start_date : ", data_splitted[3], "To")
                new_start_date = input()
                while not re.search(date_regex, new_start_date):
                    print("enter a valid date:")
                    new_start_date = input()

                print("Change yout old end_date : ", data_splitted[4], "To")
                new_end_date = input()
                while not re.search(date_regex, new_end_date):
                    print("please enter a valid date")
                    new_end_date = input()

                data_splitted[0] = new_Title
                data_splitted[1] = new_Details
                data_splitted[2] = new_total_target
                data_splitted[3] = new_start_date
                data_splitted[4] = new_end_date

            joined_data = ':'.join(data_splitted)
            new_list.append(joined_data)

        
        my_data = ''.join(new_list)

        update_file = open('project_data.txt', 'w')
        update_file.write(my_data)
        update_file.close()

    except FileNotFoundError:
        print("file not found ", FileNotFoundError)

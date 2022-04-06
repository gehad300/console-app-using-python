import project.create_project as create
import project.update_project as update
import project.delete_project as delete
import project.search_project as search
import project.view_projects as view_all

def sub_menue(email):
    my_crud = {
         "create_project": 1,
           "update_project": 2,
           "view_projects":3,
           "delete":4,
           "search":5,
           "exit":6
             }
    print("please choose from 1 to 6: ")
    for key,value in my_crud.items():
      print(f"{key}:{value}")
    user_choice=int(input("your choice will be : \n"))
      
    if user_choice ==my_crud["create_project"]:
       
        create.create_project(email)
    elif user_choice==my_crud["update_project"]:
         
      update.update_project(email)
    elif user_choice==my_crud["view_projects"]:
          
          view_all.view_projects()
    elif user_choice ==my_crud["delete"]:   
        delete.delete_project(email)

    elif user_choice==my_crud["search"]:
       project_data=search.search_project()
       if project_data==None:
             print("not found")
       else:
              print(project_data)
    elif user_choice==my_crud["exit"]:
        exit()
   
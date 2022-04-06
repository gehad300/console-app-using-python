def view_projects():
    print("This is your projects")

    try:
         projects=open("project_data.txt",'r')
         
         for project in projects:
            split_proj=project.split(":")
            for item in split_proj:
                print(item)
            print("=====================")
        
    except FileNotFoundError:
        print("file not found",FileNotFoundError)
 
    
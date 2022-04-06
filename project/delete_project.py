def delete_project(email):
     old_Title=input("please Enter project title: ")
     new_list =[]

     try:
        data_updated=open('project_data.txt','r')
        for data in data_updated:
           data_splitted=data.split(':')
           mail=data_splitted[5] 
           email1=email+'\n'
           if data_splitted[5]==email1  and old_Title==data_splitted[0]:
              data_splitted.clear()
           
           joined_data=':'.join(data_splitted)
           new_list.append(joined_data)


        
     
        my_data=''.join(new_list)

        
        update_file=open('project_data.txt','w')
        update_file.write(my_data)
        update_file.close()
        print("===========================")
        print("You delete it successfully")
        print("============================")
    

               
              
     except FileNotFoundError:
          print("file not found ",FileNotFoundError)
                     


import register
import login
import sub_menue

def main():
    if __name__ == "__main__":
      main()

my_options = {
         "register": 1,
           "login": 2,
           "exit":3
             }
print("please choose 1 for register , 2 for login , 3 for exit :")  
option_input = int(input("your choice is :"))
if option_input == my_options["register"]:
       register.register()
elif option_input==my_options["login"]:
       login.login()
        
elif  option_input==my_options['exit']:
  exit()
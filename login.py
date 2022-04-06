import sub_menue
def login():
  
    is_found=False
    email = input(" please Enter your email: ")
    password = input(" please Enter your password: ")
    try:
        users=open('users.txt','r')
        for user in users:
            user_data=user.split(":")
            if user_data[2]==email and user_data[3]==password:
                is_found=True
    except FileNotFoundError:
        print("file not found",FileNotFoundError)
        open("users.txt",'w')

    if is_found:
        print("successfully login")
        sub_menue.sub_menue(email)
    else:
        print( "========invalid login!========")



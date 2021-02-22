import os # os module is used to run system programs
import getpass # This module is used to take some input as password and does not echo back

os.system("clear")

original_psw = "1234"
passwd = getpass.getpass("Enter the Passowrd : ")

if ( passwd != original_psw ) :
    print("Authentication Failed")
    exit()

while ( True ) :

    os.system("tput setaf 1") # tput setaf is used to set the foreground colour and 1 means red colour
    print("\n\t\t\tWelcome to Terminal User Interface")

    os.system("tput setaf 7") # 7 means white colour
    print("\t\t________________________________________________\n")

    print("\nWhere you want to perform your task (local/remote)? : ", end = '')
    location_choice = input().lower()

    print("""\n\t\t\tPress 1 for see  the current date.
             \t\tPress 2 for see the current calender.
             \t\tPress 3 to create a new user.
             \t\tPress 7 for exit.""") # Triple quotes are used to have multiple strings in single print() function

    print("\nEnter your choice : ", end = '')
    choice = input()

    #Conditional Statement Starts Here

    if ( location_choice == 'local' ) :
        if ( choice == '1' ) :
            os.system("date")

        elif ( choice == '2') :
            os.system("cal")

        elif ( choice == '3' ) :
            print("Can you tell me the User Name that you want to create : ", end = '')
            user_name = input()

            os.system("useradd {0}".format(user_name)) # format() functiom will used to fill the input value of user_name inside the curly_braces({})

            print("\nDo you want to check whether the User has been created or not(y/n)? : ", end = '')
            is_user_created = input().lower()

            if ( is_user_created == 'y' ) :
                os.system("id {}".format(user_name))

            else :
                exit()

        elif ( choice == '7' ) :
            exit ()

        input("\nPress Enter to continue....") # This input() function will halt the screen so that we can see the output
        os.system("clear") # This will clear the screen after displaying the output and when the user hits Enter from the keyboard.

    elif ( location_choice == 'remote' ) :
        if ( choice == '7' ) :
            exit()

        print("Can you tell me the IP Address : ", end = '')
        remote_ip_address = input()

        if ( choice == '1' ) :
            os.system("ssh {0} date".format(remote_ip_address))

        elif ( choice == '2') :
            os.system("ssh {0} cal".format(remote_ip_address))

        elif ( choice == '3' ) :

            print("Can you tell me the User Name that you want to create : ", end = '')
            user_name = input()

            os.system("ssh {0} useradd {1}".format(remote_ip_address, user_name)) # format() functiom will used to fill the input value of ip_address and  user_name inside the curly_braces({})

            print("\nDo you want to check whether the User has been created or not(y/n)? : ", end = '')
            is_user_created = input().lower()

            if ( is_user_created == 'y' ) :
                os.system("ssh {0} id {1}".format(remote_ip_address, user_name))

            else :
                exit()

        input("\nPress Enter to continue.....")
        os.system("clear")

    else :
        rint(location_choice, "Location does not support")

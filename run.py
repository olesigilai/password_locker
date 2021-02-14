from user import User,Credentials

def create_new_user(username,password):
    '''
    function that creates a user using a password and username
    '''
    new_user = User(username,password) 
    return new_user
def save_user(user):
    '''
    function that saves a new user
    '''
    user.save_user()

def display_user(user):
    '''
    function that displays user
    '''
    return User.display_user()

def login_user(password,username):
    '''
    a fumction that checks if the users already exist 
    '''
    checked_user = Credentials.verify_user(password,username)
    return checked_user

def create_new_credential(account,username,password):
    '''
    function that create new credential details for a new user
    '''
    new_credential = Credentials(account,username,password)
    return new_credential

def save_credentials(credentials):
    '''
    function that addes a new credential to the credential
    '''
    credentials.save_user_credentials()

def delete_credentials(credentials):
    '''
    function that deletes credentials from the credential list
    '''
    credentials.delete_credentials()
def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_by_number(account)

def check_credentials(account):
    '''
    function that checks if the credentials of the searched name exist and return true or falsd
    '''
    return Credentials.credentials_exist(account)

def generate_password(self):
    ''' 
    function tht generates password randomly
    '''
    auto_password = Credentials.generate_password(self)
    return auto_password

def main():
    print("Hello Welcome to PasswordLocker...\n To procced enter any of the following...\n nw ---  To put up a new Account  \n lg --- Already have An Account  \n")
    short_code = input("").lower().strip()
    if short_code == 'nw':
        print("Sign Up")
        print('*' * 50)
        print("Username")
        username = input()
        print("password")
        password = ""
        while True:
            print(" TP - Type your own pasword?..\n GP - Generate from our random Password")
            pass_choice = input().lower().strip()
            if pass_choice == 'tp':
                print("\n")
                password = input("Enter Password\n")
                break
            elif pass_choice == 'gp':
                password = generate_password(password)
                break
            else:
                print("Invalid password")
        save_user(create_new_user(username,password))
        print("*"*60)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*60) 
    elif short_code == "lg":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 40)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username} welcome to PasswordLocker" )
            print("\n")
    while True:
        print("To proceed select any:\n CC - Create a new credential  \n FC - Find a credential \n GP - Generate a randomn password \n D - Delete credential \n EX - Exit the application \n")    
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credentials")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            username = input()
            while True:
                print(" TP - Type your own pasword if you already have an account:\n GP - Generate a random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password(password)
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,username,password))
            print('\n')
            print(f"Account Credential for:Account {account} :Username: {username} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Name : {search_credential.username}")
                print('-' * 40)
                print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 40)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*40)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("The Credential you want to delete does not exist")

        elif short_code == 'gp':

            password = generate_password(password)
            print(f" {password} Successful. You use it now.")
        elif short_code == 'ex':
            print("Thanks for using PasswordLocker.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    main()
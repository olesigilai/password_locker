

class User:
    '''
    class that generate instance of user and user_list password
    '''
    user_list = []
    def __init__(self,username,password)
        self.username = username
        self.password = password
    def save_user(self):
        '''
        save_user method saves a new user object to user list
        '''
        User.user_list.append(self)
        
    def delete_user(self):
        '''
        delete_user method deletes a saved user from user_list
        '''
        User.user_list.remove(self)
    @classmethod
    def display_user(cls):
        return cls.user_list
class Credentials:
    credentials_list = []
    def __init__(self,account,username,password):
        self.account = account
        self.password = password
        self.username = username
    @classmethod
    def verify_user(cls,username,password):
        a_user = ''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
                return a_user
    def save_user_credentials(self):
        '''
        save_user_credential method saves a new user object to credentials list
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        delete saved credentials in the credentials list
        '''
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_number(cls,account):
        '''
        this method takes in password and returns a password that match that number 
        Args:
        number: password number to search for
        Returns :
        password of person that matches the number.
        '''
        
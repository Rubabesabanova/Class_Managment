from lib import *
from functions import *


def Registration():
    email = CheckEmail("email", input("PLease enter your email : "))
    if email==True:return False
    username = CheckUsername("username", input("Please enter your username : "))
    if username==True:return False
    password = CheckPassword("password", input("Please enter your password : "))
    if password==True: return False
    return [email, username, password]






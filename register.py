from lib import *
from functions import *


def Registration():
    email = CheckEmail("email", input("Please enter your email : "))
    if email==True:return -1
    username = CheckUsername("username", input("Please enter your username : "))
    if username==True:return -1
    password = CheckPassword("password", input("Please enter your password : "))
    if password==True: return -1
    return [email, username, password]






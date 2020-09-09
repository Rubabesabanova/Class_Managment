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


def addUser():
    register=input('''If you want to add a CEO, type "admin",
If you want to add a teacher, type "editor",
If you want to add a student, type "user", 
If you want to quit, type "quit",
Please type keyword :  ''').lower()
    if register=="admin":
        x=Registration()
        if x!=-1:
                admin = Admin(*x)
                admin.AddDictToJson()
    if register=="editor":
        x=Registration()
        if x!=-1:
                editor = Editor(*x)
                editor.AddDictToJson()
    if register=="user":
        x=Registration()
        if x!=-1:
                user = User(*x)
                user.AddDictToJson()



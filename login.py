from lib import *
from functions import *


def UsernameExist(x):
    usernameExists = -1
    for i in range(len(db['users'])):
        if db['users'][i]['username'] == x:
            return i
    return usernameExists

def Login():
    username=input('''Fill gaps to login. If you want to quit, type "quit",
Please enter username : ''')
    l_username=UsernameExist(username)
    while l_username==-1:
        if username == "quit":return -1
        username=input("Enter correct username : ")
        l_username=UsernameExist(username)
    if username == "quit":return -1
    password=input("Please enter password : ")
    while password!=db['users'][l_username]['password']:
        if password == "quit":return -1
        password=input("Enter correct password : ")
    if password == "quit":return -1
    return l_username

from lib import *
from functions import *
with open('db.json') as json_file:
    db = json.load(json_file)

def UsernameExist(x):
    usernameExists = False
    for i in range(len(db['users'])):
        if db['users'][i]['username'] == x:
            return i
    return usernameExists

def Login():
    username=input('''Fill gaps to login. If you want to quit, type "quit",
Please enter username : ''')
    l_username=UsernameExist(username)
    while not l_username:
        if username == "quit":return False
        username=input("Enter correct username : ")
        l_username=UsernameExist(username)
    if username == "quit":return False
    password=input("Please enter password : ")
    while password!=db['users'][l_username]['password']:
        if password == "quit":return False
        password=input("Enter correct password : ")
    if password == "quit":return False
    return l_username

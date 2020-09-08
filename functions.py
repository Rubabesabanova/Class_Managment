from lib import *


def EntryInfo():
    order = input('''If you want to register, press 1,
If you want to login, press 2 
If you want to quit, press 0
What do you want to do ? ''').lower()
    return order
def UserInfo():
    x=input('''If you want to see account, type "account",
If you want to change account, type "change",
If you want to delete account, type "delete",
If you want to quit, type "quit". 
What do you want to do? ''')
    return x
def EditorInfo():
    x=input('''If you want to see account, type "account",
If you want to change account, type "change",
If you want to delete account, type "delete",
If you want to quit, type "quit". 
What do you want to do? ''')
    return x
def AdminInfo():
    x=input('''If you want to see account, type "account",
If you want to change account, type "change",
If you want to delete account, type "delete",
If you want to quit, type "quit". 
What do you want to do? ''')
    return x
def ShowAccount(x):
    print(f'''**********************
Email : {db['users'][x]['email']}
Username : {db['users'][x]['username']}
Password : {db['users'][x]['password']}
**********************''')
def DeleteAccount(x):
    db['users'].pop(x)
    with open("db.json", "w") as json_file:
        json.dump(db, json_file)
    print("You deleted the account successfully")
    return True
def FillGaps(_name, x):
    isEmpty = False
    while not x:
        isEmpty = True
        x = input("{} can't be empty : ".format(_name.capitalize()))
    return isEmpty
def ChangeAccount(x, _list):
    db['users'][x]['email']=_list[0]
    db['users'][x]['username']=_list[1]
    db['users'][x]['password']=_list[2]
    print(db)
    with open("db.json", "w") as json_file:
        json.dump(db, json_file)

def CheckSpaceExist(_name, x):
    spaceExist = False
    for i in x:
        if i == " ":
            spaceExist = True
            print('''{} can't contain space.'''.format(_name.capitalize()))
    return spaceExist


def CheckLength(_name, _number, x):
    correctLength = True
    if len(x) < _number:
        correctLength = False
        print('''{} should be at least {} characters.'''.format(_name.capitalize(), _number))
    return correctLength





# Email validation
def CheckEmail(_name, x):
    while CheckSpaceExist(_name, x) or not CheckLength(_name, 3, x) or not CheckEmailSign(x):
        if x == "quit":return True
        x = input('Please enter your email : ')
    if x == "quit":return True
    return x


def CheckEmailSign(x):
    emailSign = True
    if '@' not in x:
        emailSign = False
        print('''Email should contain @ symbol. ''')
    return emailSign


# Username validation
def CheckUsername(_name, x):
    while FillGaps(_name, x) or CheckUsernameExist(_name, x) or CheckSymbolExist(_name, x):
        if x == "quit":return True
        x = input('''Please enter correct username : ''')
    if x == "quit":return True
    return x


def CheckUsernameExist(_name, x):
    usernameExists = False
    for i in db['users']:
        if i['username'] == x:
            usernameExists = True
            print('This {} is already taken.'.format(_name))
    return usernameExists


def CheckSymbolExist(_name, x):
    symbolExists = False
    for i in x:
        if not i.isalpha() and not i.isdigit():
            symbolExists = True
            print("{} should can't contain symbols.".format(_name.capitalize()))
            break
    return symbolExists


# Password validation
def CheckPassword(_name, x):
    while FillGaps(_name, x) or CheckSpaceExist(_name, x) or not CheckPasswordUnique(_name, x):
        if x == "quit":return True
        x = input('''Please enter correct password : ''')
    if x == "quit":return True
    return x


def CheckPasswordUnique(_name, x):
    passwordUnique = True
    if x.isalpha() or x.isdigit():
        passwordUnique = False
        print("{} can't consist of only letters or numbers.".format(_name))
    return passwordUnique

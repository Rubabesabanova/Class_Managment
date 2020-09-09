from functions import *
from register import *
from login import *
from lib import *
from system import *

def EntryOrder():
    order=EntryInfo()
    while order !="0":
        if order=="1":
            print('''Fill gaps to register. If you want to quit, type "quit"''')
            x=Registration()
            if x!=-1:
                user = User(*x)
                user.AddDictToJson()
            order=EntryInfo()
        elif order=="2":
            x=Login()
            if x!=-1:
                if db['users'][x]['role']=="User":
                    UserSystem(x)
                if db['users'][x]['role']=="Editor":
                    EditorSystem(x)
                if db['users'][x]['role']=="Admin":
                    AdminSystem(x)
            order=EntryInfo()
        else:
            order=input("Please enter correct keyword : ")
    else:
        print("Good luck!")
EntryOrder()

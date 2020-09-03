from functions import *
from register import *
from login import *
from lib import *

def EntryOrder():
    order=EntryInfo()
    while order !="0":
        if order=="1":
            print('''Fill gaps to register. If you want to quit, type "quit"''')
            x=Registration()
            if x!=False:
                user = User(*x)
                user.AddDictToJson()
            order=EntryInfo()
        elif order=="2":
            x=Login()
            if x!=False:
                if db['users'][x]['role']=="User":
                    userorder=UserInfo()
                    while True:
                        delete=False
                        if userorder=="account":
                            ShowAccount(x)
                            userorder=UserInfo()
                        if userorder=="change":
                            print('''Here is your previous information. Fill gaps to change account.
If you want to quit, type "quit"''')
                            ShowAccount(x)
                            userlist=Registration()
                            if x!=False:
                                db['users'][x]['email']=userlist[0]
                                db['users'][x]['username']=userlist[1]
                                db['users'][x]['password']=userlist[2]
                                print(db)
                                with open("db.json", "w") as json_file:
                                    json.dump(db, json_file)
                            userorder=UserInfo()
                        if userorder=="delete":
                            checkDelete=input('''Are you sure to delete the account?'
Type YES / NO    : ''').lower()
                            while True:
                                if checkDelete=='no':
                                    break
                                elif checkDelete=='yes':
                                    delete=DeleteAccount(x)
                                    break
                                else:
                                    checkDelete=("Please enter correct keyword")
                            if delete:
                                break
                            userorder=UserInfo()
                        if userorder=="quit":
                            break
                        else:
                            userorder=input("Please enter correct keyword : ")

                if db['users'][x]['role']=="Editor":
                    editororder=EditorInfo()
                    while True:
                        if editororder=="account":
                            ShowAccount(x)
                            editororder=EditorInfo()
                        if editororder=="change":
                            print('''Here is your previous information. Fill gaps to change account.
If you want to quit, type "quit"''')
                            ShowAccount(x)
                            editorlist=Registration()
                            if x!=False:
                                db['users'][x]['email']=editorlist[0]
                                db['users'][x]['username']=editorlist[1]
                                db['users'][x]['password']=editorlist[2]
                                with open("db.json", "w") as json_file:
                                    json.dump(db, json_file)
                            editororder=UserInfo()
                        if editororder=="quit":
                            break
                        else:
                            editororder=input("Please enter correct keyword : ")
                if db['users'][x]['role']=="Admin":
                    adminorder=AdminInfo()
                    while True:
                        if adminorder=="account":
                            ShowAccount(x)
                            adminorder=AdminInfo()
                        if adminorder=="quit":
                            break
                        else:
                            adminorder=input("Please enter correct keyword : ")
            order=EntryInfo()
        else:
            order=input("Please enter correct keyword : ")
    else:
        print("Good luck!")
EntryOrder()

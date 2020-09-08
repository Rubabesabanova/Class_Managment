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
            if x!=-1:
                if db['users'][x]['role']=="User":
                    userorder=UserInfo()
                    while True:
                        delete=False
                        if userorder=="account":
                            ShowAccount(x)
                        if userorder=="change":
                            print('''Here is your previous information. Fill gaps to change account.\nIf you want to quit, type "quit"''')
                            ShowAccount(x)
                            userlist=Registration()
                            if x!=-1 and userlist!=-1:
                                ChangeAccount(x, userlist)
                        if userorder=="delete":
                            checkDelete=input('''Are you sure to delete the account?'\nType YES / NO    : ''').lower()
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
                        if userorder=="quit":
                            break
                        else:
                            userorder=input("Please enter correct keyword : ")
                        userorder=UserInfo()
                if db['users'][x]['role']=="Editor":
                    editororder=EditorInfo()
                    while True:
                        if editororder=="account":
                            ShowAccount(x)
                            
                        if editororder=="change":
                            print('''Here is your previous information. Fill gaps to change account.\nIf you want to quit, type "quit"''')
                            ShowAccount(x)
                            editorlist=Registration()
                            if x!=-1 and editorlis!=-1:
                                ChangeAccount(x, editorlist)
                        if editororder=="quit":
                            break
                        else:
                            editororder=input("Please enter correct keyword : ")
                        editororder=EditorInfo()
                if db['users'][x]['role']=="Admin":
                    adminorder=AdminInfo()
                    while True:
                        if adminorder=="account":
                            ShowAccount(x)
                            
                        elif adminorder=="change":
                            print('''Here is your previous information. Fill gaps to change account.\nIf you want to quit, type "quit"''')
                            ShowAccount(x)
                            adminlist=Registration()
                            if x!=-1 and adminlist!=-1:
                                ChangeAccount(x, adminlist)
                            
                        elif adminorder=="delete":
                            checkDelete=input('''Are you sure to delete the account?'\nType YES / NO    : ''').lower()
                            while True:
                                if checkDelete=='no':
                                    break
                                elif checkDelete=='yes':
                                    delete=DeleteAccount(x)
                                    break
                                else:
                                    checkDelete=("Please enter correct keyword : ")
                            if delete:
                                break
                            
                        elif adminorder=="quit":
                            break
                        else:
                            adminorder=input("Please enter correct keyword : ")
                        adminorder=AdminInfo()
            order=EntryInfo()
        else:
            order=input("Please enter correct keyword : ")
    else:
        print("Good luck!")
EntryOrder()

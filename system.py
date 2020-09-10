from functions import *
from register import *
from login import *
from lib import *
from products_functions import *

def UserSystem(x):
    userorder = UserInfo()
    while True:
        delete = False
        if userorder == "account":
            ShowAccount(x)
        elif userorder == "change":
            print('''Here is your previous information. Fill gaps to change account.\nIf you want to quit, type "quit"''')
            ShowAccount(x)
            userlist = Registration()
            if x != -1 and userlist != -1:
                ChangeAccount(x, userlist)
        elif userorder == "delete":
            checkDelete = input(
                '''Are you sure to delete the account?'\nType YES / NO    : ''').lower()
            while True:
                if checkDelete == 'no':
                    break
                elif checkDelete == 'yes':
                    delete = DeleteAccount(x)
                    break
                else:
                    checkDelete = ("Please enter correct keyword")
            if delete:
                break
        elif userorder=="allproducts":
            ShowAllProducts()
        elif userorder=="buy":
            BuyProduct()
        elif userorder == "quit":
            break
        else:
            print("Please enter correct keyword : ")
        userorder = UserInfo()
def EditorSystem(x):
    editororder=EditorInfo()
    while True:
        if editororder=="account":
            ShowAccount(x)       
        elif editororder=="change":
            print('''Here is your previous information. Fill gaps to change account.\nIf you want to quit, type "quit"''')
            ShowAccount(x)
            editorlist=Registration()
            if x!=-1 and editorlis!=-1:
                ChangeAccount(x, editorlist)
        elif editororder=="delete":
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
        elif editororder=="user":
            ShowUsers()
        elif editororder=="allproducts":
            ShowAllProducts()
        elif editororder=="quit":
            break
        else:
            print("Please enter correct keyword : ")
        editororder=EditorInfo()
def AdminSystem(x):
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
        elif adminorder=="adduser":
            addUser()
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
        elif adminorder=="all":
            ShowAll()
        elif adminorder=="addproduct":
            AddProduct()
        elif adminorder=="allproducts":
            ShowAllProducts()
        elif adminorder=="changeproduct":
            ChangeProduct()
        elif adminorder=="deleteproduct":
            DeleteProduct()
        elif adminorder=="quit":
            break
        else:
            print("Please enter correct keyword : ")
        adminorder=AdminInfo()
UserSystem(2)
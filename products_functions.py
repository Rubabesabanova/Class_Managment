from lib import *
from functions import *
def CreateProduct():
    print('''Please fill the gaps : ''')
    name = CheckName("name", input("Name : "))
    if name==True:return -1
    id = CheckID("ID", input("ID : "))
    if id==True:return -1
    price = CheckPrice("price", input("Price : "))
    if price==True:return -1
    amount = CheckAmount("amount", input("Amount : "))
    if amount==True:return -1
    print(amount)
    return [name, id, price, amount]
def AddProduct():
    x=CreateProduct()
    if x!=-1:
        product=Product(*x)
        product.AddToJson()
        print("Successfully added ! ")
def ShowAllProducts():
    if len(db['products'])>0:
        for i in db['products']:
            print(f'''~:~:~:~:~:~:~:~:~:~:~:~:
Name : {i['name']}
ID : {i['id']}
Price : {i['price']}
Amount : {i['amount']}
~:~:~:~:~:~:~:~:~:~:~:~:''')
    else:
        print('There is no products left')
def ChangeProduct():
    id=CheckProduct(input("ID : "))
    if id!=-1:
        x=CreateProduct()
        db['products'][id]["name"]=x[0]
        db['products'][id]["id"]=x[1]
        db['products'][id]["price"]=x[2]
        db['products'][id]["amount"]=x[3]
        with open("db.json", "w") as json_file:
                json.dump(db, json_file)
    print("You changed succesfully ! ")
def CheckProductExists(x):
    idExists = -1
    for i in range(len(db['products'])):
        if db['products'][i]['id'] == x:
            idExists = i
            break
    if id==-1:
        print("There is no such product ! ")
    return idExists
    
def CheckProduct(x):
    id=CheckProductExists(x)
    while id==-1:
        if x=="quit": return -1
        x=input("Please enter correct ID : ") 
        id=CheckProductExists(x) 
    if x=="quit": return -1
    return id
def DeleteProduct():
    id=CheckProduct(input("ID : "))
    if id!=-1:
        while True:
            x=input("YES / NO ? ").lower()
            if x=="yes":
                del db['products'][id]
                with open("db.json", "w") as json_file:
                    json.dump(db, json_file)
                print("You deleted successfully ! ")
                break
            elif x=="no":
                break
            else:
                print("Type correct keyword ! ")
# Name validation 
def CheckName(_name, x):
    while FillGaps(_name, x) or CheckSymbolExist(_name, x):
        if x == "quit": return True
        x = input('''Please enter correct name : ''')
    if x == "quit":return True
    return x
# ID validation
def CheckID(_name, x):
    while FillGaps(_name, x) or not CheckLength(_name, 3, x) or CheckIDExist(_name, x) or CheckNumber(_name, x):
        if x == "quit": return True
        x = input('''Please enter correct ID : ''')
    if x == "quit":return True
    return x

def CheckIDExist(_name, x):
    idExists = False
    for i in db['products']:
        if i['id'] == x:
            idExists = True
            print('This {} is already taken.'.format(_name))
    return idExists
# Price validation
def CheckPrice(_name, x):
    while True:
        try:
            x=float(x)
            break
        except:
            if x == "quit": return True
            x=input(f"{_name.capitalize()} must be numeric value!")
    if x == "quit":return True
    return x
def CheckAmount(_name, x):
    while CheckNumber(_name, x):
        if x=="quit": return True
        x=input("Enter correct amount : ")
    if x == "quit":return True
    return x
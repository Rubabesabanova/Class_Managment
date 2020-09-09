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
    return [name, id, price]
def AddProduct():
    x=CreateProduct()
    if x!=-1:
        product=Product(*x)
        product.AddToJson()
        print("Successfully added ! ")
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
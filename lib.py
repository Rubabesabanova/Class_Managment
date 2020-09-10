import json

with open("db.json") as json_file:
    db = json.load(json_file)


class User:
    def __init__(self, _email, _username, _password):
        self.email = _email
        self.username = _username
        self.password = _password
        self.role = "User"

    def AddToDict(self):
        return {
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "role": self.role,
        }

    def AddDictToJson(self):
        db['users'].append(self.AddToDict())
        with open("db.json", "w") as json_file:
            json.dump(db, json_file)


class Editor(User):
    def __init__(self, _email, _username, _password):
        super(Editor, self).__init__(_email, _username, _password)
        self.role = "Editor"



class Admin(User):
    def __init__(self, _email, _username, _password):
        super(Admin, self).__init__(_email, _username, _password)
        self.role = "Admin"


class Product:
    def __init__(self, _name, _id, _price, _amount):
        self.name=_name
        self.id=_id
        self.price=_price
        self.amount=_amount
    def TurnToDict(self):
        return {
            "name": self.name,
            "id": self.id,
            "price": self.price,
            "amount": self.amount
        }
    def AddToJson(self):
        db['products'].append(self.TurnToDict())
        with open("db.json", "w") as json_file:
            json.dump(db, json_file)

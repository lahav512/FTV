from flask import Flask, jsonify, request

app = Flask(__name__)

def sendOK(msg):
    return {"ok": str(msg)}

def sendError(msg):
    return {"error": str(msg)}

class Database:
    next_id = 2
    data = {
        0: {
            "name": "Lahav",
            "password": "1234"
        },
        1: {
            "name": "Daniel",
            "password": "1234"
        }
    }

    @classmethod
    def addUser(cls, name, password):
        cls.data[cls.next_id] = {
            "name": name,
            "password": password
        }
        cls.next_id += 1
        return cls.next_id - 1

    @classmethod
    def isUserExist(cls, name):
        return bool([0 for i in Database.data.values() if i["name"] == name])

class Server:

    @staticmethod
    @app.route("/")
    def root():
        return "Server side."

    @staticmethod
    @app.route("/Users/Database")
    def usersDatabase():
        return jsonify(Database.data)

    @staticmethod
    @app.route("/Users/register", methods=["GET", "POST"])
    def usersRegister():
        name = request.form["name"]
        password = request.form["password"]

        if Database.isUserExist(name):
            return sendError("This username is already exist.")
        else:
            return sendOK(Database.addUser(name, password))


if __name__ == '__main__':
    app.run(port=80, debug=True)

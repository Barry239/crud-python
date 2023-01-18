from pymongo import MongoClient
from bson import ObjectId

from models import User

class DBConnection:
    DB_HOST = 'localhost:27017'
    DB_NAME = 'pycrud'

    def __getDBConnection(self):
        return MongoClient(f'mongodb://{self.DB_HOST}/')

    def createUser(self, user: User):
        conn = self.__getDBConnection()
        db = conn[self.DB_NAME]
        collection = db['users']

        data = { 'username': user.getUsername(), 'email': user.getEmail() }
        collection.insert_one(data)

        conn.close()

    def getUsers(self):
        conn = self.__getDBConnection()
        db = conn[self.DB_NAME]
        collection = db['users']

        users = [User(row['_id'], row['username'], row['email']) for row in collection.find()]

        conn.close()

        return users

    def getUser(self, id):
        conn = self.__getDBConnection()
        db = conn[self.DB_NAME]
        collection = db['users']

        row = collection.find_one({ '_id': ObjectId(id) })
        user = User(row['_id'], row['username'], row['email'])

        conn.close()

        return user

    def updateUser(self, id, user):
        conn = self.__getDBConnection()
        db = conn[self.DB_NAME]
        collection = db['users']

        data = { '$set': { 'username': user.getUsername(), 'email': user.getEmail() } }
        collection.update_one({ '_id': ObjectId(id) }, data)

        conn.close()

    def deleteUser(self, id):
        conn = self.__getDBConnection()
        db = conn[self.DB_NAME]
        collection = db['users']

        collection.delete_one({ '_id': ObjectId(id) })

        conn.close()

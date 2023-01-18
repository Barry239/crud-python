from mysql import connector
from models import User

class DBConnection:
    DB_HOST = 'localhost'
    DB_NAME = 'pycrud'
    DB_USER = 'root'
    DB_PWD = 'n0m3l0'

    def __getDBConnection(self):
        return connector.connect(
            host=self.DB_HOST,
            database=self.DB_NAME,
            user=self.DB_USER,
            password=self.DB_PWD
        )

    def createUser(self, user):
        conn = self.__getDBConnection()
        cursor = conn.cursor(prepared=True)

        query = "INSERT INTO users(username, email) VALUES (%s, %s)"
        cursor.execute(query, (user.getUsername(), user.getEmail(),))

        conn.commit()

        cursor.close()
        conn.close()

    def getUsers(self):
        conn = self.__getDBConnection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM users"
        cursor.execute(query)

        users = [User(row['id'], row['username'], row['email']) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return users

    def getUser(self, id):
        conn = self.__getDBConnection()
        cursor = conn.cursor(dictionary=True, prepared=True)

        query = "SELECT * FROM users WHERE id=%s"
        cursor.execute(query, (id,))

        row = cursor.fetchone()
        user = User(row['id'], row['username'], row['email'])

        cursor.close()
        conn.close()

        return user

    def updateUser(self, id, user):
        conn = self.__getDBConnection()
        cursor = conn.cursor(prepared=True)

        query = "UPDATE users SET username=%s, email=%s WHERE id=%s"
        cursor.execute(query, (user.getUsername(), user.getEmail(), id,))

        conn.commit()

        cursor.close()
        conn.close()

    def deleteUser(self, id):
        conn = self.__getDBConnection()
        cursor = conn.cursor(prepared=True)

        query = "DELETE FROM users WHERE id=%s"
        cursor.execute(query, (id,))

        conn.commit()

        cursor.close()
        conn.close()

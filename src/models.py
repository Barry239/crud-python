class User:
    def __init__(self, id=None, username=None, email=None):
        self.__id = id
        self.__username = username
        self.__email = email

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setUsername(self, username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email
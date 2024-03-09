import mysql.connector
import os

class MySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    def connect(self):
        try:
            if(self.connection == None):
                self.connection = mysql.connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.password,
                    database = self.database
                )
                os.system("color a2")
                print("Wow, me conecte")
        except mysql.connector.Error as error:
            print("Error mientras se estaba conectando {}".format(error))

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close
                self.connection = None
        except mysql.connector.Error as error:
            print("Error")
    
    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as error:
            print(f"Error : {error}")

db = MySQL("localhost", "root","","testlp")
print("Conectado")

db.connect()
#categorias = db.execute_query("Select * from categorias")
#db.disconnect()
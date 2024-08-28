import sqlite3
connection = sqlite3.connect("EB_Bill")
print("Database opened successfully")
cursor = connection.cursor()
#delete
#cursor.execute('''DROP TABLE Address;''')
connection.execute("""CREATE TABLE "EB_Bill" ("units" INTEGER NOT NULL UNIQUE,"amount"INTEGER NOT NULL UNIQUE))""");
print("Table created successfully")
connection.close()   



import sqlite3
connection = sqlite3.connect("addressbook.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
#cursor.execute('''DROP TABLE Address;''')
connection.execute("""CREATE TABLE "Address" ("id"	INTEGER,"name"	TEXT NOT NULL,"email"	TEXT NOT NULL UNIQUE,"address"	TEXT NOT NULL,
	"mobilenum"	INTEGER,PRIMARY KEY("mobilenum","id"))""");
print("Table created successfully")
connection.close()   

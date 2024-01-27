import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
    # 'WHERE id= "3"'
)

for column in cursor.fetchall():
    # _id = column[0]
    # name = column[1]
    # weight = column[2]
    _id,name,weight = column
    print(_id,name,weight)
    

cursor.close()
connection.close() 

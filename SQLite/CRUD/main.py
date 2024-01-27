import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "bd.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# DELETE SEM WHERE
cursor.execute(
    f"DELETE FROM {TABLE_NAME}"
)

# DELETE COM WHERE
# Zerando IDs
cursor.execute(
    f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'"
)
connection.commit()

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)
connection.commit()

# Registrar valores nas colunas da tabela

# ABAIXO TEM RISCO DE SQL INJECTION
# cursor.execute(
#     f"INSERT INTO {TABLE_NAME} (id, name, weight)"
#     "VALUES (NULL, 'Wendell', '60'), (NULL, 'William', '70')"
# ) 

# PREVININDO SQL INJECTI0N (PASSANDO COMANDOS SEPARADOS)
sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight)'
    'VALUES'
    '(:name, :weight)'
)

# cursor.execute(sql, ["Luis Otavio", 75])
# cursor.executemany(sql, [["Luis Otavio", 75], ["Helena", 60]])
# cursor.executemany(
    # sql,
    # (
    #     ("Luis Otavio", 75), ("Helena", 60)
    # )

cursor.execute(sql, {'name': 'Luis Otavio', 'weight': 75})
cursor.executemany(sql, (
    {'name': 'Nome 1', 'weight': 65},
    {'name': 'Nome 2', 'weight': 75},
    {'name': 'Nome 3', 'weight': 85},
    {'name': 'Nome 4', 'weight': 80},
    {'name': 'Nome 5', 'weight': 63}
))
connection.commit()

if __name__ == "__main__":

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name= "NEW NAME", weight= 67 '
        'WHERE id= "5"'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for column in cursor.fetchall():
        print(column)

    cursor.close()
    connection.close()

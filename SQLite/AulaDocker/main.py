import pymysql
import pymysql.cursors
import dotenv
import os

dotenv.load_dotenv()

TABLE_NAME = "customers"

connection = pymysql.connect(
    host = os.environ["MYSQL_HOST"],
    user = os.environ["MYSQL_USER"],
    password = os.environ["MYSQL_PASSWORD"],
    database = os.environ["MYSQL_DATABASE"],
    charset= "utf8mb4",
    cursorclass= pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # Isso limpa a tabela
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME} ')
        connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Leon', 18)
        result = cursor.execute(sql, data)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = (
            {"age": 41, "name": "Sah" },
            {"age": 16, "name": "John" },
            {"age": 62, "name": "Robert" },
            )
        result = cursor.executemany(sql, data2)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 22, ),
            ("Helena", 15, ),
        )
        result = cursor.executemany(sql, data4)
    connection.commit()

    with connection.cursor() as cursor:
        # menor_id = input("Digite o menor id: ")
        # maior_id = input("Digite o maior id: ")
        menor_id = 2
        maior_id = 4
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            # 'WHERE id >= %s AND id <= %s ' a mesma coisa do de baixo
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))

        data5 = cursor.fetchall()
        for row in data5:
            print(row)
    
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql,(1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome= %s, idade=%s '
            'WHERE id = %s'
        )
        cursor.execute(sql,("Eleonor",102, 4))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # data5 = cursor.fetchall()
        # for row in data5:
        #     print(row)

        data5 = cursor.fetchall()
        for row in data5:
            print(row)
            # print(row["nome"])


    # ITENS INTERESSANTES: PARA DADOS ROBUSTOS, MUITO GRANDES
            
        # cursor.scroll(-2) Volta duas linha apos o inter se esgotar
        # cursor.scroll(5, "absolute") a partir da linha 5
        
        # SSCursor -> fetchall.unbuffered = generator
            # if row["id"] >= 5:
                # break
            
        # scroll nao é muito usado , pois nao funciona corretamente
        # len(data5) quant linhas afetadas
        
        # cursor.execute(
        #     f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1 '
        # )
        # lastid = cursor.fetchone()
        # print(lastid) ultima row mudada

        # cursor.rownumber() qual row o cursor esta

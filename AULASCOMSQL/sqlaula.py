import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='postgres',
    user='Lorena',
    password='1234'
)

conn.autocommit = True

#definir um novo banco de dados
db_name = 'db_mundotech'

#criar uma string sql para ser executada
create_db_query = sql.SQL('CREATE DATABASE {}').format(sql.Identifier(db_name))

# Construindo um cursor
cur = conn.cursor()
cur.execute(create_db_query)

# fechando a conexão do banco
cur.close()
conn.close()

print(f"Banco de dados '{db_name}' criado com sucesso!")

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database=db_name,
    user='Lorena',
    password='1234'
)

conn.autocommit = False

create_table_query = '''
    CREATE TABLE nome_tabela (
    coluna1 VARCHAR(255),
    coluna2 VARCHAR(255)
    )
'''

cur = conn.cursor()
cur.execute(create_table_query)
conn.commit()
cur.close()
conn.close()

print("Tabela criada com sucesso!")


# INSERT
valor1 = 'valor1'
valor2 = 'valor2'
cur.execute('INSERT INTO nome_tabela (coluna1, coluna2) VALUES (%s, %s)', (valor1, valor2))
conn.commit()

# SELECT
cur.execute('SELECT * FROM nome_tabela')
rows = cur.fetchall()
for row in rows:
    print(row)

# UPDATE
novo_valor1 = 'novo_valor1'
valor_criterio = 'valor1'
cur.execute('UPDATE nome_tabela SET coluna1 = %s WHERE coluna1 = %s', (novo_valor1, valor_criterio))
conn.commit()

cur.execute('SELECT * FROM nome_tabela')
rows = cur.fetchall()
for row in rows:
    print(row)

# DELETE
cur.execute('DELETE FROM nome_tabela WHERE coluna2 = %s', (valor2,))
conn.commit()

cur.execute('SELECT * FROM nome_tabela')
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()


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

db_name = 'db_mundotech'
create_db_query = sql.SQL('CREATE DATABASE {}').format(sql.Identifier(db_name))



#AJUDOU O CÓDIGO A RODAR, MAS O BANCO DE DADOS JÁ EXISTE, ENTÃO O ERRO É IGNORADO
try:
    with conn.cursor() as cur:
        cur.execute(create_db_query)
        print(f"Banco de dados '{db_name}' criado com sucesso!")
except psycopg2.errors.DuplicateDatabase:
    print(f"Banco de dados '{db_name}' já existe.")
finally:
    conn.close()

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database=db_name,
    user='Lorena',
    password='1234'
)
conn.autocommit = False




create_table_query = '''
CREATE TABLE IF NOT EXISTS nome_tabela (
    coluna1 VARCHAR(255),
    coluna2 VARCHAR(255)
)
'''

with conn.cursor() as cur:
    cur.execute(create_table_query)
    print('Tabela criada com sucesso!')

    valor1 = 'valor1'
    valor2 = 'valor2'
    cur.execute(
        'INSERT INTO nome_tabela (coluna1, coluna2) VALUES (%s, %s)',
        (valor1, valor2)
    )
    conn.commit()
    print('Inserção realizada com sucesso!')

conn.close()

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import text

# Conectar ao banco de dados PostgreSQL
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
connection = engine.connect()

# Função para obter consulta SQL do usuário
def get_user_sql():
    sql = input("Insira a consulta SQL: ")
    return sql

# Executar consulta SQL inserida pelo usuário
def execute_sql(sql):
    result = connection.execute(text(sql))
    return result

try:
    # Loop para permitir múltiplas consultas
    while True:
        user_sql = get_user_sql()
        if user_sql.lower() == "exit":
            break  # Saia do loop se o usuário digitar 'exit'
        result = execute_sql(user_sql)

        # Exibir resultados
        for row in result:
            print(row)

except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")

finally:
    # Fechar conexão ao final
    connection.close()

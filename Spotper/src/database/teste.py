# pylint: disable=all
from database import DatabaseService

db_service = DatabaseService()

# Inserindo um registro
db_service.insert("INSERT INTO users (nome, idade) VALUES (%s, %s)", ("Alice", 30))

# Procurando registros
users = db_service.search("SELECT * FROM users WHERE idade > %s", (25,))
for user in users:
    print(user)

# Fechando a conexão
db_service.close_connection()

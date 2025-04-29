from .user_repository import UserRepository
from src.models.settings.db_connection_handly import db_connection_handler
import pytest

@pytest.fixture(autouse=True)
def setup_database():
    # Conecta ao banco de dados
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    
    # Cria a tabela users se não existir
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            balance INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    
    yield  # Aqui os testes serão executados
    
    # Limpeza após os testes (opcional)
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()

def test_repository():
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = "Bob Esponja"
    password = "123Rocket!"

    # Testa o registro
    user = repo.get_user_by_username(username)
    print()
    print(user)
    
    # Verifica se o usuário foi inserido
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    assert result is not None
    assert result[1] == username  # username está na posição 1

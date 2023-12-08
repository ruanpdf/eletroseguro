import psycopg2.extras
from .banco import get_conexao


def cadastrar_cliente(nome, senha, email, data_nascimento, telefone):
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(
        """
        INSERT INTO clientes (nome, senha, email, data_nascimento, telefone)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (nome, senha, email, data_nascimento, telefone),
    )
    conn.commit()
    cursor.close()
    conn.close()


def verificar_cliente(email, senha):
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(
        """
        SELECT * FROM clientes WHERE email = %s AND senha = %s
        """,
        (email, senha),
    )
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()
    return cliente

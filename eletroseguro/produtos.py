import psycopg2.extras
from .banco import get_conexao


def get_produtos():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos


def get_produto_por_id(produto_id):
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM produtos WHERE id = %s", (produto_id,))
    produto = cursor.fetchall()[0]
    cursor.close()
    conn.close()
    return produto


def get_produto_por_nome(nome):
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM produtos WHERE nome ILIKE %s", (f"%{nome}%",))
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos

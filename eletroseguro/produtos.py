from .banco import get_conexao


def get_produtos():
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos


def get_produto_por_id(id):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos


def get_produto_por_nome(nome):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE nome LIKE %s", (f"%{nome}%",))
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos

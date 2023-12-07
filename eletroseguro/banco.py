import psycopg2


def iniciar_banco():
    conn = psycopg2.connect(
        database="eletroseguro", user="postgres", password="root", host="localhost"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            senha VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            data_nascimento DATE NOT NULL,
            telefone VARCHAR(20) NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            preco FLOAT NOT NULL,
            avaliacao FLOAT NOT NULL,
            total_vendidos INTEGER NOT NULL,
            imagem VARCHAR(255) NOT NULL,
            descricao TEXT NOT NULL
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()


def get_conexao():
    return psycopg2.connect(
        database="eletroseguro", user="postgres", password="root", host="localhost"
    )


def inserir_produtos():
    conn = get_conexao()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM produtos")
    total_de_produtos = cursor.fetchone()[0]
    if total_de_produtos > 0:
        return

    cursor.execute(
        """
        INSERT INTO produtos (nome, preco, avaliacao, total_vendidos, imagem, descricao)
        VALUES ('Smart TV LED 50" UHD 4K Samsung 50TU8000 Crystal UHD, Borda Infinita, Alexa Built In, Visual Livre de Cabos, Modo Ambiente Foto, Controle Único - 2020', 2699.99, 4.5, 100, './produtos/tv.jpg', 'Smart TV LED 50" UHD 4K Samsung 50TU8000 Crystal UHD, Borda Infinita, Alexa Built In, Visual Livre de Cabos, Modo Ambiente Foto, Controle Único - 2020')
        """
    )

    cursor.execute(
        """
        INSERT INTO produtos (nome, preco, avaliacao, total_vendidos, imagem, descricao)
        VALUES ('Smartphone Samsung Galaxy A71 128GB Azul 6GB RAM', 1999.99, 4.5, 100, './produtos/celular.jpg', 'Smartphone Samsung Galaxy A71 128GB Azul 6GB RAM')
        """
    )

    cursor.execute(
        """
        INSERT INTO produtos (nome, preco, avaliacao, total_vendidos, imagem, descricao)
        VALUES ('Notebook Acer Aspire 3 A315-42G-R2LK AMD Ryzen 7 12GB RAM 1TB HD 15,6" Windows 10', 3999.99, 4.5, 100, './produtos/notebook.jpg', 'Notebook Acer Aspire 3 A315-42G-R2LK AMD Ryzen 7 12GB RAM 1TB HD 15,6" Windows 10')
        """
    )

    cursor.execute(
        """
        INSERT INTO produtos (nome, preco, avaliacao, total_vendidos, imagem, descricao)
        VALUES ('Smartwatch Xiaomi Mi Band 4 Preto', 199.99, 4.5, 100, './produtos/smartwatch.jpg', 'Smartwatch Xiaomi Mi Band 4 Preto')
        """
    )

    conn.commit()
    cursor.close()
    conn.close()

from flask import Flask, render_template
from eletroseguro.banco import iniciar_banco, inserir_produtos
from eletroseguro.produtos import get_produtos, get_produto_por_id, get_produto_por_nome
from flask import request

app = Flask(__name__)
iniciar_banco()
inserir_produtos()


@app.route("/")
def pagina_inicial():
    return render_template("inicio.html")


@app.route("/produtos")
def pagina_produtos():
    if "nome" in request.args:
        nome = request.args["nome"]
        produtos = get_produto_por_nome(nome)
        return render_template("produtos.html", produtos=produtos)
    else:
        produtos = get_produtos()
        return render_template("produtos.html", produtos=produtos)


@app.route("/produtos/<int:id>")
def pagina_detalhar_produto(id):
    produto = get_produto_por_id(id)
    return render_template("detalhe_produto.html", produtos=produto)


@app.route("/contato")
def pagina_contato():
    return render_template("contato.html")

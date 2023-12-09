from flask import Flask, render_template, redirect
from eletroseguro.banco import iniciar_banco, inserir_produtos
from eletroseguro.produtos import get_produtos, get_produto_por_id, get_produto_por_nome
from eletroseguro.clientes import cadastrar_cliente, verificar_cliente
from flask import request

app = Flask(__name__)
iniciar_banco()
inserir_produtos()


@app.route("/inicio")
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
    return render_template("detalhe_produto.html", produto=produto)


@app.route("/")
def pagina_contato():
    return render_template("contato.html")


@app.route("/login", methods=["GET", "POST"])
def pagina_login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        cliente = verificar_cliente(email, senha)

        if cliente:
            return redirect("/inicio")
        return render_template("login.html", erro="Usuário ou senha incorretos")
    else:
        return render_template("login.html")


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        email = request.form.get("email")
        data_de_nascimento = request.form.get("data_de_nascimento")
        telefone = request.form.get("telefone")
        cadastrar_cliente(nome, senha, email, data_de_nascimento, telefone)
        return redirect("/login")
    else:
        return render_template("cadastrar.html")

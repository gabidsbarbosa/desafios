from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL


def create_app():
    from app import routes
    routes.init_app(app)

    return app


app = Flask(__name__)

# conexão com o banco de dados
app.config['MYSQL_Host'] = 'localhost' # 127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'gabes'
app.config['MYSQL_DB'] = 'desafios'

mysql = MySQL(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/quemsomos")
def quem_somos():
    return render_template('quemsomos.html')

@app.route('/contato', methods=['GET', 'POST'])
def contatos():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        mysql.connection.commit()
        cur.close()
        return 'sucesso'
    return render_template('contato.html')


# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM desafios.contato")
    if users != "":
        userDetails = cur.fetchall()
        return render_template('users.html', userMessages=userDetails)
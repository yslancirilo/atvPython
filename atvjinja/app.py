from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome = "Yslan"
    return render_template('index.html', nome=nome)

@app.route('/user')
def user():
    dados = {"nome" : "Joao" , "idade" : "67"}
    return render_template('user.html' , dados=dados )

@app.route('/dados')
def dados():
    usuario = {"nome": "Ana", "email": "ana@email.com"}
    return render_template('dados.html', usuario=usuario)

@app.route('/lista')
def lista():
    alunos = ['Ana', 'Bruno', 'Carlos', 'Diana']
    return render_template('lista.html', alunos=alunos)

@app.route('/nota')
def notas():
    alunos = [
        {'nome': 'Ana', 'notas': 8.5},
        {'nome': 'Bruno','notas': 7.0},
        {'nome': 'Carlos','notas': 9.0},
        {'nome': 'Diana','notas': 6.5}
    ]
    return render_template('nota.html' , notas=alunos )

if __name__ == '__main__':
    app.run(debug=True)

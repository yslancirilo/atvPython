from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body {
                font-family: Arial, sans-serif;
                background: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            h2 {
                margin-bottom: 20px;
                color: #333;
                text-align: center;
            }
            form {
                background: #fff;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                width: 300px;
            }
            input {
                width: 100%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
            button {
                width: 100%;
                padding: 10px;
                background: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover { background: #45a049; }
        </style>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    usarios = [
        {'usuario': 'dolga', 'senha': 'cotemig2026'},
        {'usuario': 'janaina', 'senha': 'cotemig2026'},
        {'usuario': 'antonio', 'senha': 'cotemig2026'},
        {'usuario': 'yslan', 'senha': '1234'},
    ]
    for user in usarios:
        if user['usuario'] == usuario and user['senha'] == senha:
            return '<h2>Olá {}!</h2>'.format(usuario)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)
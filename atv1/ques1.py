from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

@app.route("/decorator")
def decorator():
	return ''' O que é? 
    Um Decorator é uma função que "envolve" outra função. Ele funciona como uma moldura: você adiciona novas funcionalidades ao redor do código original sem precisar modificá-lo internamente. 

    Para que serve? 
    - Reutilização: Evita repetir código em várias funções (DRY).
    - Separação de Preocupações: Mantém a lógica principal limpa, movendo tarefas secundárias (como segurança ou logs) para o decorator.
    - Controle: Permite executar ações antes e depois da função principal ser chamada. \n

    Uso Comum (Exemplos):
    - Autenticação: Conferir se o usuário tem permissão.
    - Logging: Registrar quando uma ação foi feita.
    - Timing: Medir quanto tempo uma tarefa demora.
    

    No Flask: @app.route
    No Flask, o decorator é o mapeador. Ele conecta uma URL (rota) a uma função Python.

    Ação: Quando o navegador acessa meusite.com/contato, o decorator @app.route("/contato") intercepta o acesso e diz ao Flask: "Ei, execute a função logo abaixo e envie a resposta para o usuário!".

    Exemplo Python:
    @app.route("/contato")  # <-- O Decorator (O "Onde")
    def pagina_contato():   # <-- A Função (O "O Que")
        return "Fale conosco!"
    '''




if __name__ == "__main__":
	app.run(debug=True)

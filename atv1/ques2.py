from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"


@app.route("/curriculo")
def curriculo():
	return ''' 
  <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Currículo - Yslan Cirilo</title>
    </head>
    <body>
        <h1>YSLAN CIRILO PEREIRA PARREIRAS</h1>
        <ul>
            <li>17 Anos</li>
            <li>Contagem, Minas Gerais</li>
            <li>(31) 99809-2239</li>
            <li>yslanciriloppay@gmail.com</li>
        </ul>

        <h2>OBJETIVO</h2>
        <p>Estudante de Informática com interesse em desenvolvimento de Inteligência Artificial, Machine Learning e Segurança da Informação. Busco oportunidades para aplicar meus conhecimentos, desenvolver novas habilidades e contribuir com projetos inovadores.</p>

        <h2>FORMAÇÃO ACADÊMICA</h2>
        <ul>
            <li>
                <strong>Ensino Médio e Técnico em Informática (Cursando – 3º Ano)</strong>
                <br>Colégio Cotemig Floresta (Fev/2025 – Dez/2026)
            </li>
            <li>
                <strong>Ensino Fundamental e Médio Técnico</strong>
                <br>Sesi Alvimar Carneiro de Rezende (Fev/2015 – Dez/2023)
            </li>
            <li>
                <strong>Sesi BH Horto</strong>
                <br>(Fev/2024 – Dez/2024)
            </li>
        </ul>

        <h2>EXPERIÊNCIA</h2>
        <ul>
            <li>
                <strong>Escoteiro – Grupo 107º GEVIT (2019 – 2025)</strong>
                <ul>
                    <li>Desenvolvimento de liderança, trabalho em equipe e resolução de problemas.</li>
                    <li>Habilidades em sobrevivência, primeiros socorros e orientação.</li>
                    <li>Tomada de decisões sob pressão e desenvolvimento de pensamento estratégico.</li>
                </ul>
            </li>
        </ul>

        <h2>COMPETÊNCIAS</h2>
        <h3>Tecnologia</h3>
        <ul>
            <li>Conhecimento intermediário em hardware e software.</li>
            <li>Back-end e Front-end (Intermediário).</li>
            <li>Bancos de dados (Intermediário).</li>
            <li>Modelagem 3D no Blender.</li>
            <li>Manutenção e montagem de computadores (Intermediário).</li>
            <li>Robótica (Intermediário).</li>
            <li>Inteligência Artificial (Intermediário).</li>
            <li>Domínio das ferramentas do Google (Docs, Sheets, Slides, Drive).</li>
        </ul>
        
        <h3>Produtividade e Análise</h3>
        <ul>
            <li>Conhecimento intermediário em Excel.</li>
        </ul>

        <h3>Habilidades Técnicas</h3>
        <ul>
            <li>Experiência em robótica e automação.</li>
        </ul>

        <h2>IDIOMAS</h2>
        <ul>
            <li>Inglês – B2 (Intermediário)</li>
        </ul>

        <h2>PRÊMIOS E CERTIFICAÇÕES</h2>
        <ul>
            <li>Oficina de Robótica Sesi – 2022</li>
            <li>Oficina de Robótica Sesi – 2023</li>
            <li>Medalha de Bronze – OBA (Olimpíada Brasileira de Astronomia) – 2024</li>
            <li>Certificado Proerd – 2019</li>
			<li>CODCLUB COTEMIG (Projeto social) - 2026</li>
        </ul>
    </body>
    </html>
    '''


if __name__ == "__main__":
	app.run(debug=True)

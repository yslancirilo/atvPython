import math
from flask import render_template, request


def calcular():
    operacao = request.form["operacao"]
    num1 = float(request.form["num1"])

    def _render(etapas, resultados):
        return render_template("calculadora.html", etapas=etapas, resultados=resultados)

    if operacao == "sqrt":
        if num1 < 0:
            return _render(f"Não existe raiz real de {num1}.", "Erro: número negativo")
        r = math.sqrt(num1)
        return _render(f"√{num1}", r)

    if operacao == "log":
        if num1 <= 0:
            return _render(f"Logaritmo indefinido para {num1}.", "Erro: número inválido")
        r = math.log10(num1)
        return _render(f"log₁₀({num1})", r)

    if operacao == "bhaskara":
        b = float(request.form.get("num2", 0) or 0)
        c = float(request.form.get("num3", 0) or 0)
        a = num1
        delta = b**2 - 4 * a * c
        if delta < 0:
            return _render(f"Δ = {b}² − 4·{a}·{c} = {delta}", "Sem raízes reais (Δ < 0)")
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        etapas = f"Δ = {b}² − 4·{a}·{c} = {delta} | x = (−{b} ± √{delta}) / (2·{a})"
        return _render(etapas, f"x₁ = {x1:.4f}  |  x₂ = {x2:.4f}" if delta > 0 else f"x = {x1:.4f}")

    num2_str = request.form.get("num2", "").strip()
    if not num2_str:
        return _render("Informe o segundo número para esta operação.", "")
    num2 = float(num2_str)

    if operacao == "+":
        return _render(f"{num1} + {num2}", num1 + num2)
    if operacao == "-":
        return _render(f"{num1} − {num2}", num1 - num2)
    if operacao == "*":
        return _render(f"{num1} × {num2}", num1 * num2)
    if operacao == "/":
        if num2 == 0:
            return _render(f"{num1} ÷ 0", "Erro: divisão por zero")
        return _render(f"{num1} ÷ {num2}", num1 / num2)
    if operacao == "**":
        return _render(f"{num1} ^ {num2}", num1 ** num2)

    return _render("Operação inválida.", "")

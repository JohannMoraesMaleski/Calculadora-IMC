from flask import Flask, render_template, request

app = Flask(__name__)

# Função para calcular IMC e classificação

def calcular_imc(peso, altura):
    if altura > 3.0:
        altura = altura / 100
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
        cor = "🔵"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
        cor = "🟢"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
        cor = "🟡"
    elif 30 <= imc < 35:
        classificacao = "Obesidade grau I"
        cor = "🟠"
    elif 35 <= imc < 40:
        classificacao = "Obesidade grau II"
        cor = "🔴"
    else:
        classificacao = "Obesidade grau III (mórbida)"
        cor = "🔴"
    return imc, classificacao, cor

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    erro = None
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            if peso <= 0 or altura <= 0:
                erro = "Peso e altura devem ser positivos."
            else:
                imc, classificacao, cor = calcular_imc(peso, altura)
                resultado = {
                    'peso': peso,
                    'altura': altura,
                    'imc': round(imc, 2),
                    'classificacao': classificacao,
                    'cor': cor
                }
        except Exception:
            erro = "Por favor, insira valores válidos."
    return render_template('index.html', resultado=resultado, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)

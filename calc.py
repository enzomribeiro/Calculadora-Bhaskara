from flask import Flask, render_template, request
import math

app = Flask(__name__)

def bhaskara(a, b, c):
    delta = (b**2) - (4 * a * c)

    if delta < 0:
        return None, None, delta  # sem raízes reais
    elif delta == 0:
        x = -b / (2 * a)
        return x, x, delta
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2, delta


@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = {}
    delta = None  # inicializa delta

    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            x1, x2, delta = bhaskara(a, b, c)

            if delta < 0:
                aviso = "Não existe raiz real"
                raizes = None
            else:
                aviso = None
                raizes = (x1, x2)

            resultado = {
                "a": a,
                "b": b,
                "c": c,
                "raizes": raizes,
                "delta": delta,
                "aviso": aviso
            }

        except ValueError:
            resultado['erro'] = "Por favor, insira valores válidos para 'a', 'b' e 'c'."

    return render_template("index.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

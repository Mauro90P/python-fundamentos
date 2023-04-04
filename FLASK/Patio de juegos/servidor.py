from flask import Flask

app = Flask(__name__)


@app.route('/play/<color>/<int:num>')
def play(color, num):
    if num < 1:
        return 'El número debe ser mayor que cero'

    html = ''
    for i in range(num):
        html += f'<div style="background-color:{color}; width:300px; height:300px; margin:20px; display:inline-block;"></div>'

    return html


if __name__ == "__main__":
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

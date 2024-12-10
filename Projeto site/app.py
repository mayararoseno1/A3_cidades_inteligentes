from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Rota para arquivos estáticos
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

# Lista de artesãos cadastrados
artisans = []

@app.route('/')
def index():
    # Exibe a página inicial com a lista de artesãos cadastrados
    return render_template('index.html', artisans=artisans)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Coletar os dados do formulário
        name = request.form['name']
        email = request.form['email']
        craft = request.form['craft']
        desired_material = request.form['desired_material']
        
        # Criar o registro do artesão
        artisan = {
            "name": name,
            "email": email,
            "craft": craft,
            "desired_material": desired_material
        }
        artisans.append

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de empresas fictícias e materiais recicláveis disponíveis
companies = [
    {"name": "Empresa A", "material": "Papelão", "location": "São Paulo"},
    {"name": "Empresa B", "material": "Plástico", "location": "Rio de Janeiro"},
    {"name": "Empresa C", "material": "Vidro", "location": "Belo Horizonte"},
    {"name": "Empresa D", "material": "Metal", "location": "Porto Alegre"},
    {"name": "Empresa E", "material": "Madeira", "location": "Curitiba"}
]

# Lista de artesãos cadastrados
artisans = []

@app.route('/')
def index():
    # Exibe a página inicial com a lista de empresas e materiais recicláveis
    return render_template('index.html', companies=companies)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        artisan = {"name": name, "email": email}
        artisans.append(artisan)
        return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

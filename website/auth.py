from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    return render_template('Index.html')

@auth.route('/formulari')
def formulari():
    return render_template('addCard.html')

@auth.route('/afegirCarta', methods=['POST'])
def afegirCarta():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        mana = request.form.get('mana')
        tipo = request.form.get('tipo')
        descripcion = request.form.get('descripcion')
        print("nombre: ",nombre, 'mana: ', mana, 'tipo: ', tipo, 'descripcion',descripcion) 
    
    return render_template('index.html')
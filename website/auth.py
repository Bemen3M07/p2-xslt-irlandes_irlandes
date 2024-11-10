from flask import Blueprint, render_template, request
import xml.etree.ElementTree as ET

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
        escriure_xml(nombre,mana,tipo,descripcion)
    
    return render_template('index.html')

   
    


def escriure_xml(nombre,mana,tipo,descripcion):
    tree = ET.parse('website/static/Cards.xml')
    root = tree.getroot()
    nova_carta = ET.Element("Carta")
    nom = ET.SubElement(nova_carta, "Nombre")
    nom.text = nombre
    
    cost_mana = ET.SubElement(nova_carta, "Mana")
    cost_mana.text = mana
    
    
    tipus_carta = ET.SubElement(nova_carta, "Tipo")
    tipus_carta.text = tipo
    
    descripcio = ET.SubElement(nova_carta, "Descripcion")
    descripcio.text = descripcion
    
    root.append(nova_carta)
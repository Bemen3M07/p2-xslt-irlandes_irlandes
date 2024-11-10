from flask import Blueprint, render_template, request
import xml.etree.ElementTree as ET

auth = Blueprint('auth', __name__)#la llibreria de Blueprint es l'encarregada de guardar totes les rutes d'aquest fitxer

@auth.route('/')#Indica la ruta necesaria perque pugis cridar la funcio
def index():
    return render_template('Index.html')#render_temlate s'encarrega de que el html estigui ven renderitzat i que carregui be al buscador

@auth.route('/formulari')
def formulari():
    return render_template('addCard.html')

@auth.route('/afegirCarta', methods=['POST'])#afegir el method per poder recolectar l'informació del html
def afegirCarta():
    if request.method == 'POST':
        nombre = request.form.get('nombre')#amb la llibreria request agafem l'informacio de cada input box
        mana = request.form.get('mana')
        tipo = request.form.get('tipo')
        descripcion = request.form.get('descripcion')
        escriure_xml(nombre,mana,tipo,descripcion)#crida la funcio enviantli les variables recollides del html
    
    return render_template('index.html')

   
    


def escriure_xml(nombre,mana,tipo,descripcion):
    tree = ET.parse('website/static/Cards.xml')#genera l'arbre del fitxer cards.xml
    root = tree.getroot()#recull l'arrel del xml
    nova_carta = ET.Element("Carta")#creem una nova carta
    
    nom = ET.SubElement(nova_carta, "Nombre")#afefim l'atribut Nombre de la carta
    nom.text = nombre #afegim el contigut de Nombre
    
    cost_mana = ET.SubElement(nova_carta, "Mana")#afefim l'atribut mana de la carta
    cost_mana.text = mana #afegim el contigut de mana
    
    
    tipus_carta = ET.SubElement(nova_carta, "Tipo")#afefim l'atribut tipo de la carta
    tipus_carta.text = tipo #afegim el contigut de tipo
    
    descripcio = ET.SubElement(nova_carta, "Descripcion")#afefim l'atribut descripcion de la carta
    descripcio.text = descripcion #afegim el contigut de descripcion
    
    root.append(nova_carta) #afegim al root la nova carta amb els seus atributs
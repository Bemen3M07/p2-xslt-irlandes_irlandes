[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/G9fQk55K)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17027388&assignment_repo_type=AssignmentRepo)


## Com executar el projecte
1. Descarregar python 3.13: https://www.python.org/downloads/

2. Instalem pip al cmd/consola de visual studio:py -m pip install --upgrade pip

3. Instalem la llibreria de Flask:  py -m pip install flask

4. Instalem la llibreria Flask-login: py -m pip install flask-login

5. Per utilitzar la web nomes fa falta executar el main.py i mirar la consola on sortirà una ip, la insertem al buscador o fem control+ click i sens obrirà directament.
Running on http://127.0.0.1:5000

En cas de que sortís l’error, ModuleNotFounError: No module named ‘flask’:
Farem control+shift+p (visual studio code), s’obrira un buscador en el cual posarem Python interpreter i escollirem l'última versió que tinguem instalada.

Així pots utilitzar la nostra web feta amb flask.




# Execici 1
## HTML
Utilitzem bootstrap `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">` per a fer el css amb mes facilitat.
També Django, un framework de Python utilitzamble a HTML, serveix per a tenir una base en blocs de text o imatges, que cambien depenent el contingut dels contenidors `{% block content%}`, despres aquest contenidors es poden omplir amb codi HTML `<div class="container mt-5">`.


## XML
Creem un xml que, contingui les Cartes, cada Carta, conte un nom, un manà, un tipus, i una descripcio.

Amb `<?xml-stylesheet type="text/xsl" href="showCard.xsl"?>`, linquegem el nostre XML amb el XSL.


## XSLT
Dintre del XSL creem una estroctura de web amb html.
Per a mostrar les cartes, usarem `<xsl:for-each select="Carta">`, i per agafar el contingut utilitzarem `<xsl:value-of select="Nombre"/>`, amb cada un sels elements que volguem mostrar.


# Exercici 3
Nosaltres hem escollit Flask per poder fer el formulari, el que fem al html de addCard es fer un Form amb method=POST que crida la funcio d'afegir carta del auth.py `<form action="/afegirCarta" method="POST">`. Un cop es fa click al boto submit es crida el codi de pyhton el cual utilitzant la llibreria Request que es de Flask agafem l'informacio que l'usuari a posat al formulari, despres cridem a la funcio excriure xml pasant les variables recolectades 
`escriure_xml(nombre,mana,tipo,descripcion)`, el cual s'encarrega d'escriure el xml.

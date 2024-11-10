from website import crear_aplicacio

app = crear_aplicacio()

if __name__ == '__main__':
    app.run(debug=True) #es l'encarregat de que l'aplicacio funcioni, s'ha dexecutar aqui el codi per obrir el servidor, crida la funcio feta al __init__.py
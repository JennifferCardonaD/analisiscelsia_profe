import random

def generadorDatosProducto():
    productos=["Musica","Tv","Aplicaciones","PC","Celulares","Tablets","Accesorios"]
    datos=[]
    for producto in productos:
        protCategoria={}        
        categoria=random.choice(["Plus","Mega","Basic"])
        protCategoria=[producto,categoria]
        datos.append(protCategoria)
    return datos
print (generadorDatosProducto())

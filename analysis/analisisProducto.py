from generators.generadorProducto import generadorDatosProducto
import pandas as pd

def analizarDatos():
    datos=generadorDatosProducto()
    tabla=pd.DataFrame(datos,columns=["producto","categoria"])
    tabla.to_csv("./data/producto.csv",index=False)
analizarDatos()
pandas
import pandas as pd
from Flask import Flask

app=Flask(name)

base=pd.read_excel("BaseBTR.xlsx")
def Principal():
  return "Esta es una API que te muetra Los albumnes de BTR"

@app.route("/Por_Numero/<Numero>")
def porNumero(Numero):
  fila=base[base["Numero"]==Numero]
  respuesta=f"El pokemon {Numero}es {fila. loc[:,'Nombre']}"
  return resultados

@app.route("/Por_Tipo/<Tipo>")
  def portipo(Tipo):
    resultados=base[base["Tipo"]==Tipo]
    return resultados

@app.route("/Por_Nombre/<PesNombre1>/<Nombre2>")
  def PorNombre(Nombre1,Nombre2):
    resultados=base[(base["Nombre"]>Nombre1) & (base["Nombre"]<Nombre2)]
    return resultados

if name=="main":
  app.run()

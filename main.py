pandas
import pandas as pd
from Flask import Flask

app=Flask(name)

base=pd.read_excel("BaseBTR.xlsx")

@app.route("/Por_Numero/<Numero>")
def porNumero(Numero):
  fila=base[base["Numero"]==Numero]
  respuesta=f"El pokemon {Numero}es {fila. loc[:,'Nombre']}"
  return resultados

@app.route("/Por_Tipo/<Tipo>")
  def portipo(Tipo):
    resultados=base[base["Tipo"]==Tipo]
    return resultados

@app.route("/Por_Peso/<Peso1>/<Peso2>")
  def PorPeso(Peso1,Peso2):
    resultados=base[(base["Peso"]>Peso1) & (base["Peso"]<Peso2)]
    return resultados

if name=="main":
  app.run()

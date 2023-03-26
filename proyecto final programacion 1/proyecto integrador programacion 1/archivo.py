import csv



listaderecetas = []
receta= {
    'Nombre':'',
    'Ingredientes':'',
    'Preparcion':'',
    'Imagen_Plato':'',
    'Tiempo_Prep':0,
    'Tiempo_Coc':0,
    'Fecha_Crea':'',
    'Etiqueta':'',
    'Favorita:':False
}

def creaarchivo():
      with open ("Receta.csv","w") as archivo:
         w= csv.dictwriter (archivo, receta[0].keys())
         w.writeheader()

def csv_lista():
    with open("Receta.csv", newline="") as archivo:
     lector = csv.reader(archivo, delimiter=",")
     for fila in lector:    # desempacamos las columnas en variables
        print("exist")

def csv_dict():
   encabezado=("Nombre","Ingredientes","Preparcion","Tiempo_Prep","Tiempo_Coc","Fecha_Crea","Imagen_Plato","Etiqueta","Favorita")
   with open ("Receta.csv", newline="" ) as archivo:
      lector = csv.DictReader(archivo,fieldnames=encabezado, delimiter="," )
      for rece in lector:
            print(rece["Nombre"],rece["Ingredientes"],rece["Preparcion"],rece["Tiempo_Prep"],rece["Tiempo_Coc"],
                  rece["Imagen_Plato"],rece["Etiqueta"],rece["Favorita"])

def elimina(receta):
    with open("Receta.csv","w+") as archivo:
      w = csv.DictWriter (archivo , receta[0].keys())
      #w.writeheader() graba las cabeceras
      for rece in listaderecetas:
       w.writerow(rece)

def sobreescribe(receta):
    with open("Receta.csv","w+") as archivo:
      w = csv.DictWriter (archivo , receta[0].keys())
      w.writeheader() #graba las cabeceras
      for rece in listaderecetas:
       w.writerow(rece)

def cargaarchivo(receta):
    with open("Receta.csv","a") as archivo:
      w = csv.DictWriter (archivo , receta[0].keys())
      #w.writeheader() #graba las cabeceras
      for rece in listaderecetas:
       w.writerow(rece)

def agregarrecetas(receta):
 listaderecetas.append(receta)
 cargaarchivo(listaderecetas)

def agregardatos(nombre,ingredientes,preparacion,tiempoprep,tiempococ,fechacreac,imagen=None,etiqueta=None,favorita=False):
 receta= {'Nombre':nombre,
    'Ingredientes':ingredientes,
    'Preparcion':preparacion,
    'Tiempo_Prep':tiempoprep,
    'Tiempo_Coc':tiempococ,
    'Fecha_Crea':fechacreac,
    'Imagen_Plato':imagen,
    'Etiqueta':etiqueta,
    'Favorita:':favorita}
 agregarrecetas(receta)
 

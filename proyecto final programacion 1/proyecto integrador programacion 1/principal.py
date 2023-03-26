""" creacion de ventana"""
import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from datetime import datetime
import csv
from tkinter import filedialog #para abrir directorios y buscar imagenes
from PIL import ImageTk, Image #para mostrar la imagen en la app
import archivo
from typing import Any, Hashable, Iterable, Optional
import random



class Ventana:
 
   def __init__(self, window1):
      self.window1 = window1
      self.window1.title("Recetario")
      self.window1.geometry("920x450")
      #self.window1.attributes('-fullscreen',1) # pantalla completa
      
      #Variables de busquedas
      self.busqueda=tk.StringVar() #si todo falla buscar solo con esta variable para recorrer el diccionario
      self.rbbuscar=tk.StringVar()
      #self.nombrereceta = tk.StringVar() #ver de usar un radiobuttom
      #self.etiquetareceta = tk.StringVar()
      #self.tiempoprep = tk.StringVar()
      #self.ingrediente = tk.StringVar()

      #Marco de ventana
      marco=LabelFrame(self.window1,text='ABM de  Recetas')
      marco.grid(row=0,column=0,columnspan=10,pady=20, padx=20,sticky=W+E)
      #Buscador de recetas
      Label(marco,text='Receta:').grid(row=0,column=0,columnspan=2)
      self.e_busqueda = Entry(marco, textvariable=self.busqueda)
      self.e_busqueda.grid(row=1,column=0,columnspan=10)
      
      #Boton Busqueda
      self.buscar = Button(marco,text='Buscar ....',width=20,command=self.buscar_receta)
      self.buscar.grid(row=1,column =20,columnspan=10,sticky=(W+E))
      #Boton de Creacion Nueva receta
      self.nuevareceta = ttk.Button(marco,text='Nueva Receta',width=20,command=self.nueva_receta)
      self.nuevareceta.grid(row=2,column = 0, columnspan=10,sticky=(W+E))
      #Boton Modificar una receta
      self.modificarreceta = ttk.Button(marco,text='Modificar Receta',width=20,command=self.modificar_receta)
      self.modificarreceta.grid(row=2,column = 10, columnspan=10,sticky=(W+E))
      #Boton Eliminar una receta
      self.eliminarreceta = ttk.Button(marco,text='Eliminar Receta',width=20, command=self.eliminar_receta)
      self.eliminarreceta.grid(row=2,column = 20, columnspan=10,sticky=(W+E))
      #Boton Acualizar
      self.actualizar=Button(marco,text='Refrescar Listado',width=20,command=self.update_table)
      self.actualizar.grid(row=2, column=30,columnspan=10,sticky=(W+E))
      #Boton para mostrar receta seleccionada
      self.mostrar=Button(marco,text='Mostrar Receta',width=20,command=self.mostrar_receta)
      self.mostrar.grid(row=2, column=43, columnspan=10,sticky=(W+E))                           
      #Radiobutton para la busqueda
      self.rbbuscar.set('Nombre')
      self.rb_buscar_n= ttk.Radiobutton(marco,text='Nombre', variable=self.rbbuscar,value='Nombre').grid(row=1,column=11)
      self.rb_buscar_e= ttk.Radiobutton(marco,text='Etiqueta', variable=self.rbbuscar,value='Etiqueta').grid(row=1,column=12)
      
      
      #Tabla Recetas
      
      self.tabla=ttk.Treeview(self.window1,selectmode=tk.BROWSE,columns=("Nombre","Ingredientes",'Preparcion',"Tiempo_Prep","Tiempo_Coc","Fecha_Crea","Imagen_Plato","Etiqueta",'Favorita:'))
      self.tabla.grid(row=4,column=0, columnspan=9)
     
      self.tabla.column("#0",minwidth=0,width=0)
      self.tabla.column("#1",width=100)
      self.tabla.column("#2",width=100)
      self.tabla.column("#3",width=100)
      self.tabla.column("#4",width=100)
      self.tabla.column("#5",width=100)
      self.tabla.column("#6",width=100)
      self.tabla.column("#7",width=100)
      self.tabla.column("#8",width=100)
      self.tabla.column("#9",width=100)
      self.tabla.heading('Nombre',text='Nombre Receta',anchor=CENTER)
      self.tabla.heading('Ingredientes',text='Ingredientes', anchor=CENTER)
      self.tabla.heading('Preparcion',text='Preparacion',anchor=CENTER)
      self.tabla.heading('Tiempo_Prep',text='Tiempo de Preparacion',anchor=CENTER)
      self.tabla.heading('Tiempo_Coc',text='Tiempo de Coccion',anchor=CENTER)
      self.tabla.heading('Fecha_Crea',text='Fecha de Creacion',anchor=CENTER)
      self.tabla.heading('Imagen_Plato',text='Imagen',anchor=CENTER)
      self.tabla.heading('Etiqueta',text='Etiqueta',anchor=CENTER)
      self.tabla.heading('Favorita:',text='Favorito',anchor=CENTER)
      #cargamos el archivo al treeview
      #self.update_table()
      with open(r"Receta.csv", newline="") as archivo:
        lector = csv.DictReader(archivo, delimiter=",")
        for fila in lector:
          nombre = fila['Nombre']
          ingredientes= fila['Ingredientes']
          preparacion= fila['Preparcion']
          tiempoprep= fila['Tiempo_Prep']
          tiempococ= fila['Tiempo_Coc']
          fechacreac= fila['Fecha_Crea']
          imagen= fila['Imagen_Plato']
          etiqueta= fila['Etiqueta']
          favorita= fila['Favorita:']
          self.tabla.insert("",0,values=(nombre,ingredientes,preparacion,tiempoprep,tiempococ,fechacreac,imagen,etiqueta,favorita))
      lista=list(self.tabla.get_children())
      item=random.choice(lista)
      self.tabla.tag_configure("item",foreground='red',background='yellow')
      self.tabla.selection_set(item)
      self.tabla.focus(item)
      self.tabla.item(item,tags='item')
      
      
       
   
   def update_table(self):
      """csv a treeview"""
      self.eliminarreceta.config(state='enabled')
      self.tabla.delete(*self.tabla.get_children())
      with open("Receta.csv", newline="") as archivo:
        lector = csv.DictReader(archivo, delimiter=",")
        for fila in lector:
          nombre = fila['Nombre']
          ingredientes= fila['Ingredientes']
          preparacion= fila['Preparcion']
          tiempoprep= fila['Tiempo_Prep']
          tiempococ= fila['Tiempo_Coc']
          fechacreac= fila['Fecha_Crea']
          imagen= fila['Imagen_Plato']
          etiqueta= fila['Etiqueta']
          favorita= fila['Favorita:']
          self.tabla.insert("",0,values=(nombre,ingredientes,preparacion,tiempoprep,tiempococ,fechacreac,imagen,etiqueta,favorita))
      lista=list(self.tabla.get_children())
      item=random.choice(lista)
      self.tabla.tag_configure("item",foreground='red',background='yellow')
      self.tabla.selection_set(item)
      self.tabla.focus(item)
      self.tabla.item(item,tags='item')    
      
   
   def buscar_receta(self):
       """Funcion para buscar recetas en la tabla"""
       self.eliminarreceta.config(state='disabled')
       print(self.tabla.get_children())
       abuscar=self.busqueda.get()
       print(abuscar)
       if self.rbbuscar.get()=='Nombre':
        
        for item in self.tabla.get_children():
           cadena=self.tabla.set(item,'Nombre')
           if abuscar == cadena:
             item1=self.tabla.item(item)['values']
             self.tabla.delete(*self.tabla.get_children())
             self.tabla.insert("",0,values=(item1))
             self.e_busqueda.delete(0,END)
             print(item1)
             print(cadena)
       
       elif self.rbbuscar.get()== 'Etiqueta':
        for item in self.tabla.get_children(): 
            cadena=self.tabla.set(item,'Etiqueta')
            if abuscar == cadena:
             item2=self.tabla.item(item)['values']
             self.tabla.delete(*self.tabla.get_children())
             self.tabla.insert("",0,values=(item2))
             print(item2)
             print(cadena) 
             self.e_busqueda.delete(0,END) 
       
        else:
           messagebox.showerror(title="No hay elemento", message="Lo que busca no esta en el Recetario")

   def nueva_receta(self):
        # creamos la ventana para crear una nueva receta
        # como padre indicamos la ventana principal
        window1.state("iconic")
        toplevel = tk.Toplevel(self.window1)
        # agregamos el frame (NuevaReceta) a la ventana (toplevel)
        NuevaReceta(toplevel).grid()

   def modificar_receta(self):
        # creamos la ventana para modificar una receta
        # como padre indicamos la ventana principal
        window1.state("iconic")
        toplevel = tk.Toplevel(self.window1)
        # agregamos el frame (ModificarReceta) a la ventana (toplevel)
        diccionario=[]
        for items in self.tabla.get_children():
            new_dict = {}

            for col, item2 in zip(self.tabla["columns"],self.tabla.item(items)['values']):
                new_dict[col]=item2

            diccionario.append(new_dict)
       
       
        selected_item=self.tabla.selection()[0]
        valores=self.tabla.item(selected_item)['values']
        ModificarReceta(toplevel,valores,diccionario).grid()

   def mostrar_receta(self):
        # creamos la ventana para mostrar una receta
        # como padre indicamos la ventana principal
        toplevel = tk.Toplevel(self.window1)
        # agregamos el frame (ModificarReceta) a la ventana (toplevel)
        diccionario=[]
        for items in self.tabla.get_children():
            new_dict = {}

            for col, item2 in zip(self.tabla["columns"],self.tabla.item(items)['values']):
                new_dict[col]=item2

            diccionario.append(new_dict)
       
       
        selected_item=self.tabla.selection()[0]
        valores=self.tabla.item(selected_item)['values']
        MostrarReceta(toplevel,valores,diccionario).grid()    

   def eliminar_receta(self):
        # eliminamos el registro sellecionado del treeview, creamos una nueva lista de recetas y la grabamos en el archivo
        item=self.tabla.selection()[0]
        self.tabla.delete(item)
        valores=[]
        for items in self.tabla.get_children():
            new_dict = {}

            for col, item2 in zip(self.tabla["columns"],self.tabla.item(items)['values']):
                new_dict[col]=item2

            valores.append(new_dict)
        print (valores)
        with open("Receta.csv","w+") as archivo:
          w = csv.DictWriter (archivo , valores[0].keys())
          w.writeheader() 
          for rece in valores:
           w.writerow(rece)          


class NuevaReceta(ttk.Frame):
    """Crea la ventana para agregar nuevas recetas al recetario y proporciona los comandos necesarios para
    insertar los valores en un archivo csv"""
    def __init__(self, window1):
        super().__init__(window1, padding=(20))
        self.toplevel = window1
        window1.title("Nueva Receta")
        window1.geometry("950x350+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        window1.columnconfigure(0, weight=1)
        window1.rowconfigure(0, weight=1)
        window1.resizable(False, False)
        window1.attributes('-topmost',True)
        #Variables
        self.nombrereceta = tk.StringVar()
        self.ingre=tk.StringVar()
        self.paso=tk.StringVar()
        self.fecha_creacion = tk.StringVar()
        self.tiempo_prep = tk.IntVar()
        self.tiempo_coc =tk.IntVar()
        self.etiqueta=tk.StringVar()
        self.imagenplato=tk.StringVar()
        self.favorito=tk.BooleanVar()
        #Captura la fecha y hora que sera la de creacion de la receta *para la hora se debe agregar ",%H:%M:%S" al final
        self.mensaje=datetime.now().strftime("%d/%m/%Y")
        #Marco de ventana
        marco=LabelFrame(window1,text='Receta Nueva')
        marco.grid(row=0,column=0,rowspan= 100, columnspan=50,pady=20, padx=20,sticky=N+S+W+E)
        
        #Labels y Entrys para que se cargen los datos
        Label(marco,text='Nombre de Receta:').grid(row=0,column=0,columnspan=2)
        self.e_1=Entry(marco, textvariable=self.nombrereceta)
        self.e_1.grid(row=0,column=3,columnspan=2)
        Label(marco,text='Tiempo de Preparación:').grid(row=0,column=6,columnspan=2)
        self.e_2=Entry(marco, textvariable=self.tiempo_prep,width=10)
        self.e_2.grid(row=0,column=8,columnspan=2)
        Label(marco,text='Tiempo de Cocción:').grid(row=0,column=11,columnspan=2)
        self.e_3=Entry(marco, textvariable=self.tiempo_coc,width=10)
        self.e_3.grid(row=0,column=13,columnspan=2)
        Label(marco,text='Fecha de Creación:').grid(row=0,column=16,columnspan=2)
        Label(marco,text=self.mensaje).grid(row=0,column=20,columnspan=2)
        Label(marco,text='Etiqueta:').grid(row=1,column=0,columnspan=2)
        self.e_4=Entry(marco, textvariable=self.etiqueta,width=10)
        self.e_4.grid(row=1,column=3,columnspan=2)
        Checkbutton(marco,text='Favorito',variable=self.favorito).grid(row=1,column=5)
        #cargamos los ingredientes y los pasos de a uno en un listbox
        
        self.scrolying=Scrollbar(marco,orient="vertical")
        self.scrolxing=Scrollbar(marco,orient="horizontal")
        self.scrolying.grid(column=10,row=2,sticky=(W,N,S)) 
        self.scrolxing.grid(column=8,row=3,columnspan=2,sticky=(W,N,E))
        self.scrolypre=Scrollbar(marco,orient="vertical")
        self.scrolxpre=Scrollbar(marco,orient="horizontal")
        self.scrolypre.grid(column=10,row=4,sticky=(W,N,S))
        self.scrolxpre.grid(column=8,row=5,columnspan=2,sticky=(W,N,E))
        
        Label(marco,text='Ingredientes:').grid(row=2,column=0,columnspan=2)
        self.e_ingredientes=Entry(marco,textvariable=self.ingre)
        self.e_ingredientes.grid(row=2,column=3,columnspan=2)
        self.l_ingredientes=Listbox(marco,width=20, height=3)
        self.l_ingredientes.grid(row=2,column=8,columnspan=2)
       
        btn_cargaringre= Button(marco,text='--->',command= self.carga_ingrediente)
        btn_cargaringre.grid(row=2,column=5, columnspan=2)
        
        Label(marco,text='Pasos:').grid(row=4,column=0,columnspan=2)
        self.e_pasos=Entry(marco,textvariable=self.paso)
        self.e_pasos.grid(row=4,column=3,columnspan=2)
       
        btn_cargarpaso= Button(marco,text='--->',command=self.carga_paso )
        btn_cargarpaso.grid(row=4,column=5, columnspan=2)     
        
        self.preparacion=Listbox(marco,width=20 ,height=3)
        self.preparacion.grid(row=4,column=8,columnspan=2)
        
        #manejo de imagen
        self.img_label = Label(marco)
        self.img_label.grid(row=3, column=15, padx=5, pady=5, columnspan=2)
        self.imagenplato.set("")
        bt_cargarimagen = Button(marco, text="Cargar imagen", command=self.cargar_imagen)
        bt_cargarimagen.grid(row=4, column=15, padx=5, pady=5, columnspan=2)
        #Boton Guardar
        bt_guardar= Button(marco, text="Guardar...", command=self.agregardatos)
        bt_guardar.grid(row=50,column=0,columnspan=2)
        #Boton Cancelar
        Button(marco, text="Cancelar...", command=self.cerrar).grid(row=50,column=3,columnspan=2)
        self.scrolying.config(command=self.l_ingredientes.yview)
        self.scrolxing.config(command=self.l_ingredientes.xview)
        self.scrolypre.config(command=self.preparacion.yview)
        self.scrolxpre.config(command=self.preparacion.xview)

    def cerrar(self):
     """Cierra la Ventana actual y devuelve la pantalla principal al su tamaño normal"""
     self.toplevel.destroy()
     window1.deiconify()

    def carga_ingrediente(self):
        """cargamos los ingredientes del entry al listbox"""
        ingrediente=self.ingre.get()
        self.l_ingredientes.insert(END,ingrediente)
        self.l_ingredientes.config(yscrollcommand=self.scrolying.set,xscrollcommand=self.scrolxing.set)
        self.e_ingredientes.delete(0,END)
     

    def carga_paso(self):
        """cargamos los pasos del entry al listbox"""
        pasito=self.paso.get()
        self.preparacion.insert(END,pasito)
        self.preparacion.config(yscrollcommand=self.scrolypre.set,xscrollcommand=self.scrolxpre.set)
        self.e_pasos.delete(0,END)   
      

     

    def agregardatos(self):
        """llamamos al modulo archivo para agregar la receta y limpiamos los entrys"""
        self.toplevel.attributes('-topmost',0)
        mensaje , mensaje1, mensaje2, mensaje3, mensaje4 , mensaje5='','','','','',''
        if self.nombrereceta.get() == "":
         mensaje1 = 'Nombre'
         mensaje= mensaje1
         messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")
        elif self.tiempo_prep.get() == 0 :
         mensaje2= 'Tiempo Preparacion'
         mensaje = mensaje1 + ' ' + mensaje2
         messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")        
        elif self.tiempo_coc.get() == 0 :
          mensaje3='Tiempo de Cocion'
          mensaje = mensaje1 + ' ' + mensaje2 + ' '+mensaje3
          messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")
        elif  self.l_ingredientes.size() == 0:
          mensaje4='Ingredientes'
          mensaje = mensaje1 + ' ' + mensaje2 + ' ' + mensaje3 +' '+ mensaje4
          messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")
        elif   self.preparacion.size() ==0:
          mensaje4='Ingredientes'
          mensaje = mensaje1 + ' ' + mensaje2 + ' ' + mensaje3 +' '+ mensaje4+' '+ mensaje5
          messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")


        else:
         archivo.agregardatos(self.nombrereceta.get(),self.l_ingredientes.get(0,END),self.preparacion.get(0,END),self.tiempo_prep.get(),self.tiempo_coc.get(),self.mensaje,self.imagenplato.get(),self.etiqueta.get(),self.favorito.get())
         self.e_1.delete(0,END)
         self.e_2.delete(0,END)
         self.e_3.delete(0,END)
         self.e_4.delete(0,END)
         self.l_ingredientes.delete(0,END)
         self.preparacion.delete(0,END)
         messagebox.showinfo(title="Operación Exitosa",message="Receta agragada con Exito")

     

    
    def cargar_imagen(self):
        """Carga la imagen"""
        ruta_imagen = filedialog.askopenfilename()
        self.imagenplato.set(ruta_imagen)
        imagen = Image.open(ruta_imagen)
        imagen.thumbnail((200, 200))
        imagen = ImageTk.PhotoImage(imagen)
        self.img_label.config(image=imagen)
        self.img_label.image = imagen

    
       
       


      
class ModificarReceta(ttk.Frame):
    """Ventana para la modificacion de las recetas"""
    def __init__(self, window1,valores,diccionario):
        super().__init__(window1, padding=(20))
        self.toplevel=window1
        window1.title("Modificar Receta")
        window1.geometry("1100x450+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        window1.attributes('-topmost',True)
        window1.columnconfigure(0, weight=1)
        window1.rowconfigure(0, weight=1)
        window1.resizable(False, False)
        #Variables
        self.diccionario=diccionario
        self.values=valores
        self.nombrereceta = tk.StringVar()
        self.fecha_creacion = tk.StringVar()
        self.tiempo_prep = tk.IntVar()
        self.tiempo_coc =tk.IntVar()
        self.ingredientes=tk.StringVar()
        self.preparacion=tk.StringVar()
        self.etiqueta=tk.StringVar()
        self.imagenplato=tk.StringVar()
        self.favorito=tk.BooleanVar()
        #Captura la fecha y hora que sera la de creacion de la receta *para la hora se debe agregar ",%H:%M:%S" al final
        self.mensaje=self.values[5] #datetime.now().strftime("%d/%m/%Y")
        #Marco de ventana
        marco=LabelFrame(window1,text='Modificar Receta')
        marco.grid(row=0,column=0,rowspan= 100, columnspan=50,pady=20, padx=20,sticky=N+S+W+E)
        #Labels y Entrys para que se cargen los datos
        Label(marco,text='Nombre de Receta:').grid(row=0,column=0,columnspan=2)
        e_1=Entry(marco, textvariable=self.nombrereceta)
        e_1.grid(row=0,column=3,columnspan=2)
        e_1.insert(0,self.values[0])
        Label(marco,text='Tiempo de Preparación:').grid(row=0,column=6,columnspan=2)
        e_2=Entry(marco, textvariable=self.tiempo_prep,width=10)
        e_2.delete(0,END)
        e_2.grid(row=0,column=8,columnspan=2)
        e_2.insert(0,self.values[3])
        Label(marco,text='Tiempo de Cocción:').grid(row=0,column=11,columnspan=2)
        e_3=Entry(marco, textvariable=self.tiempo_coc,width=10)
        e_3.delete(0,END)
        e_3.grid(row=0,column=13,columnspan=2)
        e_3.insert(0,self.values[4])
        Label(marco,text='Fecha de Creacion:').grid(row=0,column=16,columnspan=2)
        Label(marco,text=self.mensaje).grid(row=0,column=20,columnspan=2)
        Label(marco,text='Etiqueta:').grid(row=1,column=0,columnspan=2)
        e_4=Entry(marco, textvariable=self.etiqueta,width=10)
        e_4.grid(row=1,column=3,columnspan=2)
        e_4.insert(0,self.values[7])
        chk_favorito=Checkbutton(marco,text='Favorito',variable=self.favorito)
        chk_favorito.grid(row=1,column=5)
        if self.values[8]=="False":
           chk_favorito.deselect()
        else:
           chk_favorito.select()

        Label(marco,text='Ingredientes:').grid(row=2,column=0,columnspan=2)
        self.e_ingredientes=Entry(marco,textvariable=self.ingredientes)
        self.e_ingredientes.grid(row=2,column=3,columnspan=2)
        
        self.scrolying=Scrollbar(marco,orient="vertical")
        self.scrolxing=Scrollbar(marco,orient="horizontal")
        self.scrolying.grid(column=13,row=2,sticky=(W,N,S))
        self.scrolxing.grid(column=11,row=3,columnspan=2,sticky=(W,N,E))
        self.scrolypre=Scrollbar(marco,orient="vertical")
        self.scrolxpre=Scrollbar(marco,orient="horizontal")
        self.scrolypre.grid(column=13,row=4,sticky=(W,N,S))
        self.scrolxpre.grid(column=11,row=5,columnspan=2,sticky=(W,N,E))
        
        self.l_ingredientes=Listbox(marco,width=20, height=3)
        self.l_ingredientes.grid(row=2,column=11,columnspan=2)
        items = list(eval(self.values[1]))
               
        self.l_ingredientes.insert(0,*items)
        self.l_ingredientes.config(yscrollcommand=self.scrolying.set,xscrollcommand=self.scrolxing.set)
        
        
        btn_cargaringre= Button(marco,text='--->',command= self.carga_ingrediente)
        btn_cargaringre.grid(row=2,column=5, columnspan=2)
        
        btn_quitaringre=Button(marco,text="<---", command=self.quitar_ingrediente)
        btn_quitaringre.grid(row=2, column=8, columnspan=2)

        Label(marco,text='Pasos:').grid(row=4,column=0,columnspan=2)
        self.e_pasos=Entry(marco,textvariable=self.preparacion)
        self.e_pasos.grid(row=4,column=2,columnspan=2)
       
        btn_cargarpaso= Button(marco,text='--->',command=self.carga_paso )
        btn_cargarpaso.grid(row=4,column=5, columnspan=2)
       
        btn_quitarpaso=Button(marco,text="<---", command=self.quitar_pasos)
        btn_quitarpaso.grid(row=4, column=8, columnspan=2)    

        self.preparacion=Listbox(marco,width=20 ,height=3)
        self.preparacion.grid(row=4,column=11,columnspan=2)
        items1 = list(eval(self.values[2]))
        self.preparacion.insert(0,*items1)
        self.preparacion.config(yscrollcommand=self.scrolypre.set,xscrollcommand=self.scrolxpre.set)
        
        self.img_label = Label(marco)
        self.img_label.grid(row=3, column=15, padx=5, pady=5, columnspan=2)
        self.imagenplato.set("")
        archivo=self.values[6]
        if archivo != '':
         print(archivo)
         print(type(archivo))
         imagen = Image.open(archivo)
         imagen.thumbnail((200, 200))
         imagen = ImageTk.PhotoImage(imagen)
         self.img_label.config(image=imagen)
         self.img_label.image = imagen
        else:
           self.imagenplato.set("")
        
        bt_cargarimagen = Button(marco, text="Cargar imagen", command=self.cargar_imagen)
        bt_cargarimagen.grid(row=6, column=15, padx=5, pady=5, columnspan=2)
        bt_quitarimagen=Button(marco,text="Quitar Imagen",command=self.quitar_imagen)
        bt_quitarimagen.grid(row=6,column=17,padx=5,pady=5,columnspan=2)

        bt_guardar= Button(marco, text="Guardar...", command=self.guardar)
        bt_guardar.grid(row=50,column=0,columnspan=2)
        Button(marco, text="Cancelar...", command=self.cerrar).grid(row=50,column=3,columnspan=2)
        self.scrolying.config(command=self.l_ingredientes.yview)
        self.scrolxing.config(command=self.l_ingredientes.xview)
        self.scrolypre.config(command=self.preparacion.yview)
        self.scrolxpre.config(command=self.preparacion.xview)

    def carga_ingrediente(self):
        """cargamos los ingredientes del entry al listbox"""
        ingrediente=self.ingredientes.get()
        self.l_ingredientes.insert(END,ingrediente)
        self.e_ingredientes.delete(0,END)

    def quitar_ingrediente(self):
        """Quitamos ingredientes del listbox"""
        item=self.l_ingredientes.curselection()[0]
        self.l_ingredientes.delete(item)
     

    def carga_paso(self):
        """cargamos los pasos del entry al listbox"""
        pasito=self.preparacion.get()
        self.preparacion.insert(END,pasito)
        self.e_pasos.delete(0,END)

    def quitar_pasos(self):
        """Quitamos pasos de la preparacion del listbox"""       
        item=self.preparacion.curselection()[0]
        self.preparacion.delete(item)       
    
   
    def buscar_dicc(self,it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
        
        for dicc in it:
         if dicc[clave] == valor:
            #print(dicc)
            #print(type(dicc))

            return dicc
        return None
    
    def guardar(self):
      """Guarda los cambios usamos la funcion buscar_dicc para encontra el diccionario dentro de la lista de recetas"""
      self.toplevel.attributes('-topmost',0)
      mensaje , mensaje1, mensaje2, mensaje3, mensaje4 , mensaje5='','','','','',''
      if self.nombrereceta.get() == "":
         mensaje1 = 'Nombre'
         mensaje= mensaje1
         messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")
      elif self.tiempo_prep.get() == 0 :
         mensaje2= 'Tiempo Preparacion'
         mensaje = mensaje1 + ' ' + mensaje2
         messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")        
      elif self.tiempo_coc.get() == 0 :
          mensaje3='Tiempo de Cocion'
          mensaje = mensaje1 + ' ' + mensaje2 + ' '+mensaje3
          messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")
      elif  self.l_ingredientes.size() == 0:
          mensaje4='Ingredientes'
          mensaje = mensaje1 + ' ' + mensaje2 + ' ' + mensaje3 +' '+ mensaje4
          messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")
      elif   self.preparacion.size() ==0:
          mensaje4='Ingredientes'
          mensaje = mensaje1 + ' ' + mensaje2 + ' ' + mensaje3 +' '+ mensaje4+' '+ mensaje5
          messagebox.showerror(title="Faltan Datos", message=f"Ingrese los datos solicitados: {mensaje}")


      else:
      
      
         new_item={'Nombre':self.nombrereceta.get(),
                 'Ingredientes':self.l_ingredientes.get(0,END),
                 'Preparcion':self.preparacion.get(0,END),
                 'Tiempo_Prep':self.tiempo_prep.get(),
                 'Tiempo_Coc':self.tiempo_coc.get(),
                 'Fecha_Crea':self.mensaje,
                 'Imagen_Plato':self.imagenplato.get(),
                 'Etiqueta':self.etiqueta.get(),
                 'Favorita:':self.favorito.get()}
      
         dictionary=self.buscar_dicc(self.diccionario,'Nombre',self.nombrereceta.get())
     
         dictionary.update(new_item)
      
         with open("Receta.csv","w+") as archivo:
          w = csv.DictWriter (archivo , self.diccionario[0].keys())
          w.writeheader() 
          for rece in self.diccionario:
           w.writerow(rece)     
         messagebox.showinfo(title="Operación Exitosa",message="Receta Modificada con Exito")
      
    def cargar_imagen(self):
        """Carga la imagen"""
        self.toplevel.attributes('-topmost', False)
        ruta_imagen = filedialog.askopenfilename()
        self.imagenplato.set(ruta_imagen)
        imagen = Image.open(ruta_imagen)
        imagen.thumbnail((200, 200))
        imagen = ImageTk.PhotoImage(imagen)
        self.img_label.config(image=imagen)
        self.img_label.image = imagen

    def quitar_imagen(self):
        self.imagenplato.set("")
        self.img_label.config(image='')

    def cerrar(self):
      """Cierra la Ventana actual y devuelve la pantalla principal al su tamaño normal"""
      self.toplevel.destroy()
      window1.deiconify()
      
       
   
 

class MostrarReceta(ttk.Frame):
     """Muestra la receta seleccionada, no permite hace modificaciones"""
     def __init__(self, window1,valores,diccionario):
        super().__init__(window1, padding=(20))
        window1.title("Modificar Receta")
        window1.geometry("1300x600+180+100")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        window1.columnconfigure(0, weight=1)
        window1.rowconfigure(0, weight=1)
        window1.resizable(False, False)
        #Variables
        self.diccionario=diccionario
        self.values=valores
        self.nombrereceta = tk.StringVar()
        self.fecha_creacion = tk.StringVar()
        self.tiempo_prep = tk.IntVar()
        self.tiempo_coc =tk.IntVar()
        self.ingredientes=tk.StringVar()
        self.preparacion=tk.StringVar()
        self.etiqueta=tk.StringVar()
        self.imagenplato=tk.StringVar()
        self.favorito=tk.BooleanVar()
        #Captura la fecha y hora que sera la de creacion de la receta *para la hora se debe agregar ",%H:%M:%S" al final
        self.mensaje=self.values[5]#datetime.now().strftime("%d/%m/%Y")
        #Marco de ventana
        marco=LabelFrame(window1,text='Mostrar Receta')
        marco.grid(row=0,column=0,rowspan= 100, columnspan=50,pady=20, padx=20,sticky=N+S+W+E)
        #Labels y Entrys para que se cargen los datos
        Label(marco,text='Nombre de Receta:').grid(row=0,column=0,columnspan=2)
       
        e_1=Entry(marco,textvariable=self.nombrereceta)
        e_1.grid(row=0,column=3,columnspan=2)
        e_1.insert(0,self.values[0])
        e_1.config(state='readonly')
       
        Label(marco,text='Tiempo de Preparación:').grid(row=0,column=6,columnspan=2)
        
        
        e_2=Entry(marco, textvariable=self.tiempo_prep,width=10)
        e_2.delete(0,END)
        e_2.grid(row=0,column=8,columnspan=2)
        e_2.insert(0,self.values[3])
        e_2.config(state='readonly')
        
        Label(marco,text='Tiempo de Cocción:').grid(row=0,column=11,columnspan=2)
        e_3=Entry(marco,textvariable=self.tiempo_coc,width=10)# state= 'readonly',
        e_3.delete(0,END)
        e_3.grid(row=0,column=13,columnspan=2)
        e_3.insert(0,self.values[4])
        e_3.config(state='readonly')
        Label(marco,text='Fecha de Modificacion:').grid(row=0,column=16,columnspan=2)
        Label(marco,text=self.mensaje).grid(row=0,column=20,columnspan=2)
        Label(marco,text='Etiqueta:').grid(row=1,column=0,columnspan=2)
        e_4=Entry(marco, textvariable=self.etiqueta,width=10)
        e_4.grid(row=1,column=3,columnspan=2)
        e_4.insert(0,self.values[7])
        e_4.config(state='readonly')
        chk_favorito=Checkbutton(marco,text='Favorito',variable=self.favorito)
        chk_favorito.grid(row=1,column=5)
        if self.values[8]=="False":
           chk_favorito.deselect()
        else:
           chk_favorito.select()
        chk_favorito.config(state='disabled')   

        Label(marco,text='Ingredientes:').grid(row=2,column=0,columnspan=2)
        
        self.scroling=Scrollbar(marco,orient=VERTICAL)
        self.scroling.grid(column=5,row=2,sticky=(W,N,S))
        self.scrolpre=Scrollbar(marco,orient=VERTICAL)
        self.scrolpre.grid(column=5,row=3,sticky=(W,N,S))
       
        self.l_ingredientes=Listbox(marco,width=50, height=10)
        self.l_ingredientes.grid(row=2,column=3,columnspan=2,sticky=(W,E))
        items = list(eval(self.values[1]))#convierte los valores al formato lista para agregar al listbox
               
        self.l_ingredientes.insert(0,*items)
        self.l_ingredientes.config(yscrollcommand=self.scroling.set)
       
        

        Label(marco,text='Pasos:').grid(row=3,column=0,columnspan=2)
        

        self.preparacion=Listbox(marco,width=50 ,height=10)
        self.preparacion.grid(row=3,column=3,columnspan=2,sticky=(W,E))
        items1 = list(eval(self.values[2]))
               
        self.preparacion.insert(0,*items1)
        self.preparacion.config(yscrollcommand=self.scrolpre.set)
        
        self.img_label = Label(marco)
        self.img_label.grid(row=2, column=8, padx=5, pady=5)
        
        Button(marco, text="Salir...", command=window1.destroy).grid(row=50,column=3,columnspan=2)
        
        archivo=self.values[6]
        print(archivo)
        print(type(archivo))
        imagen = Image.open(archivo)
        imagen.thumbnail((200, 200))
        imagen = ImageTk.PhotoImage(imagen)
        self.img_label.config(image=imagen)
        self.img_label.image = imagen
        
        
        self.scroling.config(command=self.l_ingredientes.yview)
        self.scrolpre.config(command=self.preparacion.yview)



if __name__=="__main__":
    window1=Tk()
    aplicacion=Ventana(window1)
    window1.mainloop()
    
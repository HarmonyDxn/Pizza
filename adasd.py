import tkinter
from tkinter import *
from tkinter import ttk

vSel = tkinter.Tk()
vSel.title("Tienda")
    
vSel.minsize(1000,700)
vSel.maxsize(1000,700)
vSel.iconbitmap("pittza.ico")
#imagen de fondo
img = PhotoImage(file="Pizacututu.png")
etiquetaIcono = Label(vSel,image=img)
etiquetaIcono.grid(row=0,column=0)

etiquetaIcono = Label(vSel,image=img)
etiquetaIcono.grid(row=0,column=0)

#Funciones

def guardarCliente():
    nameC=cajaCliente.get()
    print(nameC)
def guardarDireccion():
    nameD=cajaDireccion.get()
    print(nameD)
def guardarTelefono():
    nameT=cajaTelefono.get()
    print(nameT)
def guardarCorreo():
    nameCo=cajaCorreo.get()
    print(nameCo)

def agregarListaDel():
    #Falta cambiar el tipo de dato entregado a String, ya que no lo lee
    guardar=(cajaCliente)
    lista.insert(0,guardar)

def bloquearLocal():
    cajanMesa.configure(state="readonly")
    botonLocal.configure(state="disabled")
    
def bloquearDelivery():
    cajaDireccion.configure(state="readonly")
    cajaTelefono.configure(state="readonly")
    cajaCorreo.configure(state="readonly")
    botonDeli.configure(state="disabled")

def resetear ():
    cajanMesa.configure(state="normal")
    cajaDireccion.configure(state="normal")
    cajaTelefono.configure(state="normal")
    cajaCorreo.configure(state="normal")
    botonDeli.configure(state="normal")
    botonLocal.configure(state="normal")
def pagar ():
    #agregar los valores
    #hacer base de datos con los valores (ventas con su cliente respectivo)
    cajanMesa.configure(state="normal")
    cajaDireccion.configure(state="normal")
    cajaTelefono.configure(state="normal")
    cajaCorreo.configure(state="normal")
    botonDeli.configure(state="normal")
    botonLocal.configure(state="normal")
    
def listaPagado():
    pagado = tkinter.Toplevel(vSel)
    pagado.title("Pagados")
    pagado.iconbitmap("pittza.ico")
    labelPagado = tkinter.Label(pagado, text = "\nPizzas pagadas")
    labelPagado.pack()
    pagado.wm_geometry("500x400")
    listaPagado=Listbox(pagado, width=80,height=20)
    listaPagado.place(x=8,y=50)
   

def listaTrayecto():
    trayecto= tkinter.Toplevel(vSel)
    trayecto.title("Trayecto")
    trayecto.iconbitmap("pittza.ico")
    labelTrayecto = tkinter.Label(trayecto, text = "\nTrayecto de las pizzas")
    labelTrayecto.pack()
    trayecto.wm_geometry("500x400")
    listaTrayecto=Listbox(trayecto, width=80,height=20)
    listaTrayecto.place(x=8,y=50)

def listaFinalizado():
    finalizado= tkinter.Toplevel(vSel)
    finalizado.title("Finalizados")
    finalizado.iconbitmap("pittza.ico")
    labelFinalizado = tkinter.Label(finalizado, text = "\nPizzas entregadas y pagadas")
    labelFinalizado.pack()
    finalizado.wm_geometry("500x400")
    listaFinalizado=Listbox(finalizado, width=80,height=20)
    listaFinalizado.place(x=8,y=50)



ingresocli =tkinter.Label(vSel,text="Ingreso Cliente")
ingresocli.place(x=5,y=5)

nombreCliente = tkinter.Label(vSel,text="Nombre Cliente")
nombreCliente.place(x = 25,y =35)

direccion = tkinter.Label(vSel,text="Direccion")
direccion.place(x = 25,y =65)

telefono = tkinter.Label(vSel,text="Telefono")
telefono.place(x=25,y=95)

correo = tkinter.Label(vSel,text="Correo")
correo.place(x=25,y=125)

cajaCliente = tkinter.Entry(vSel)
cajaCliente.place(x=135,y=35)

cajaDireccion = tkinter.Entry(vSel)
cajaDireccion.place(x=135,y=65)

cajaTelefono = tkinter.Entry(vSel)
cajaTelefono.place(x=135,y=95)

cajaCorreo = tkinter.Entry(vSel)
cajaCorreo.place(x=135,y=125)



lcal=tkinter.Label(vSel,text="Local")
lcal.place(x=300,y=5)

nMesa=tkinter.Label(vSel,text="Numero de mesa")
nMesa.place(x=320,y=35)

cajanMesa=tkinter.Entry(vSel)
cajanMesa.place(x=480,y=35)

nPedido=tkinter.Label(vSel,text="Numero del pedido")
nPedido.place(x=320,y=65)

cajanPedido=tkinter.Entry(vSel)
cajanPedido.configure(state="readonly")
cajanPedido.place(x=480,y=65)

horaEsti=tkinter.Label(vSel,text="Hora estimada de entrega")
horaEsti.place(x=320,y=95)

cajaHora=tkinter.Entry(vSel)
cajaHora.configure(state="readonly")
cajaHora.place(x=480,y=95)

valor=tkinter.Label(vSel,text="Valor")
valor.place(x=320,y=125)

cajaValor=tkinter.Entry(vSel)
cajaValor.configure(state="readonly")
cajaValor.place(x=480,y=125)

armadoPizza=tkinter.Label(vSel,text="Armado de pizza")
armadoPizza.place(x=5,y=250)

tamaño=tkinter.Label(vSel,text="Tamaño")
tamaño.place(x=25,y=280)

#Tamaño pizza

cmbTamaño=ttk.Combobox(vSel)
cmbTamaño.place(x=135,y=280)
cmbTamaño["values"]=("Elija un tamaño","Pequeño","Mediano","Grande")
cmbTamaño.current(0)
cmbTamaño.configure(state="readonly")

masa=tkinter.Label(vSel,text="Masa")
masa.place(x=25,y=320) 

#Tipos de masa

cmbMasa=ttk.Combobox(vSel)
cmbMasa.place(x=135,y=320)
cmbMasa["values"]=("Tipo de masa","Tradicional","Delgada","Gruesa")
cmbMasa.current(0)
cmbMasa.configure(state="readonly")

ingredientes=tkinter.Label(vSel,text="Ingredientes")
ingredientes.place(x=25,y=360)

agregado=tkinter.Label(vSel,text="Agregado")
agregado.place(x=25,y=440)

#botones

botonDeli=tkinter.Button(vSel,text="Delivery",font="Arial 20",fg="blue",command=bloquearLocal)
botonDeli.place(x=40,y=170)

botonPagar=tkinter.Button(vSel,text="Pagar",font="Arial 20",fg="blue",command=agregarListaDel)
botonPagar.place(x=20,y=620)

botonLocal=tkinter.Button(vSel,text="Local",font="Arial 20",fg="blue",command=bloquearDelivery)
botonLocal.place(x=200,y=170)

botonDesacer=tkinter.Button(vSel,text="Reset",font="Arial 20",fg="blue",command=resetear)
botonDesacer.place(x=890,y=620)

botonListaPagado= tkinter.Button(vSel,text="Lista Pagado",font="Arial 20",fg="blue", command=listaPagado)
botonListaPagado.place(x=770, y= 20)


botonListaTrayecto= tkinter.Button(vSel,text="Lista Trayecto",font="Arial 20",fg="blue", command=listaTrayecto)
botonListaTrayecto.place(x=770, y= 90)

botonListaFinalizados= tkinter.Button(vSel,text="Lista Finalizados",font="Arial 20",fg="blue", command=listaFinalizado)
botonListaFinalizados.place(x=770, y= 160)

#ingredientes

cbEQueso=Checkbutton(vSel,text="Extra queso")
cbEQueso.place(x=120, y=360)

cbChampiñon=Checkbutton(vSel,text="Champiñon")
cbChampiñon.place(x=220, y=360)

cbPeperoni=Checkbutton(vSel,text="Peperoni")
cbPeperoni.place(x=320, y=360)

cbTosino=Checkbutton(vSel,text="Tosino")
cbTosino.place(x=120, y=390)

cbChoclo=Checkbutton(vSel,text="Choclo")
cbChoclo.place(x=220, y=390)

cbCebolla=Checkbutton(vSel,text="Cebolla")
cbCebolla.place(x=320, y=390)

#agregados

cbPalAjo=Checkbutton(vSel,text="Palitos de ajo")
cbPalAjo.place(x=120,y=440)

cbPalQueso=Checkbutton(vSel,text="Palitos de Queso")
cbPalQueso.place(x=230,y=440)

cbAji=Checkbutton(vSel,text="Ají")
cbAji.place(x=355,y=440)

cbCoNormal=Checkbutton(vSel,text="Cocacola")
cbCoNormal.place(x=120,y=470)

cbCoLight=Checkbutton(vSel,text="Cocacola Light")
cbCoLight.place(x=230,y=470)

cbSprite=Checkbutton(vSel,text="Sprite")
cbSprite.place(x=355,y=470)

cbSpriteLight=Checkbutton(vSel,text="Sprite Light")
cbSpriteLight.place(x=120,y=500)


vSel.mainloop()
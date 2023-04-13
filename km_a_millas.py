from tkinter import *
from tkinter import Entry


def convertir_km_millas():
    kilometros = float(entrada_km.get())
    millas = round(kilometros * 0.621,2)

    etiqueta_cnt_millas.config(text=str(millas))


ventana = Tk()
ventana.minsize(width=250,height=250)
ventana.title("KM a Millas")
ventana.config(padx=20,pady=20)

#Campo de entrada de cantidad de km
entrada_km = Entry()
entrada_km.config(width=10)
entrada_km.grid(column=1,row=0)


#Etiqueta info km
etiqueta_km = Label(text="Km",font=("Times new roman",12))
etiqueta_km.grid(column=2,row=0)

#Etiqueta es igual a ... millas
etiqueta_igual = Label(text="Es igual a ",font=("Times new roman",12))
etiqueta_igual.config(pady=10)
etiqueta_igual.grid(column=0,row=1)

#Etiqueta cantidad de millas
etiqueta_cnt_millas = Label(text="",font=("Times new roman",12))
etiqueta_cnt_millas.grid(column=1,row=1)
etiqueta_cnt_millas.config(pady=10)

#Etiqueta millas
etiqueta_millas = Label(text="Millas",font=("Times new roman",12))
etiqueta_millas.grid(column=2,row=1)
etiqueta_millas.config(pady=10)

#Boton Calcular
boton_calc = Button(text="Calcular",font=("Times new roman",12),command=convertir_km_millas)
boton_calc.grid(column=1,row=2)



ventana.mainloop()
from tkinter import *

def abrir_ventana(titulo, mensaje):
    top = Toplevel(ventana)
    top.title(titulo)
    top.geometry("300x200")
    top.config(bg="black")

    Label(top, text=mensaje,
          bg="black", fg="white", font=("Arial", 12), wraplength=250).pack(pady=20)

    Button(top, text="Cerrar", command=top.destroy,
           bg="white", fg="black", font=("Arial", 10)).pack()

ventana = Tk()
ventana.title("Juan Jose Delgado Benitez")
ventana.geometry("600x500")
ventana.resizable(False, False)
ventana.config(bg="black")

# Frame principal
frame_1 = Frame(ventana, bg="black", width=690, height=240)
frame_1.place(x=10, y=10)

# Logo opcional
logo = PhotoImage(file="img/juanjo.png")
Label_logo = Label(frame_1, image=logo)
Label_logo.place(x=10, y=10)

# Título
titulo = Label(frame_1, text="Juan Jose Delgado Benitez",
               bg="black", fg="white", font=("Arial", 16))
titulo.place(x=280, y=90)

# Subtítulo
subtitulo = Label(frame_1, text="APP DE JUANJO",
                   bg="black", fg="white", font=("Arial", 15), anchor=CENTER)
subtitulo.place(x=360, y=120)

# Botones con nombres personalizados
btn1 = Button(ventana, text="Nacimiento", width=10,
              command=lambda: abrir_ventana("nacimiento", " Naci el 10/08/2006 en el hospital Santa Cruz de la Loma, San Gil"))
btn1.place(x=50, y=300)

btn2 = Button(ventana, text="Familia", width=10,
              command=lambda: abrir_ventana("Familia", "Mama: Nidia Benitez Ortiz \n Papà:Expedito Delgado Triana\n Hermano:Diego Delgado Benitez"))
btn2.place(x=240, y=300)

btn2 = Button(ventana, text="Datos medicos", width=10,
              command=lambda: abrir_ventana("Seguro", "Nueva EPS"))
btn2.place(x=350, y=440)

btn4 = Button(ventana, text="Educacion", width=10,
              command=lambda: abrir_ventana("educacion", "donde e estudiado en mi vida"))
btn4.place(x=430, y=300)

btn5 = Button(ventana, text="amigos", width=10,
              command=lambda: abrir_ventana("amigos", "Nicolas Gonzalez y David Acosta"))
btn5.place(x=50, y=350)

btn6 = Button(ventana, text="hobbies", width=10,
              command=lambda: abrir_ventana("hobbies", "Jugar futbol"))
btn6.place(x=240, y=350)

btn7 = Button(ventana, text="horario", width=10,
              command=lambda: abrir_ventana("horario", "Voy al colegio, llego a mi casa, y aveces salgo a jugar"))
btn7.place(x=430, y=350)

btn8 = Button(ventana, text="preparacion", width=10,
              command=lambda: abrir_ventana("preparacion", "Voy a prepararme en todas las materias para tener  mejores resultados en la prueba icfes"))
btn8.place(x=145, y=400)

btn9 = Button(ventana, text="proyecto", width=10,
              command=lambda: abrir_ventana("proyecto", "Ser un comerciante"))
btn9.place(x=335, y=400)

ventana.mainloop()
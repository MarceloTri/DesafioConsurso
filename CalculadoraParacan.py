from tkinter import *
import locale

# Establece el formato de moneda dolar
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Crea la ventana principal
ventana = Tk()
ventana.geometry('500x400')
my_font = ('Arial', 14)
ventana.title('Calculadora Gráfica')

# Función para borra calculos en pantalla
def borrar_datos():
    entrada1.delete(0, END)
    entrada2.delete(0, END)
    entrada3.delete(0, END)
    entrada4.delete(0, END)
    result_text.delete('1.0', END)

# Crear los widgets
label1 = Label(ventana, text='Cantidad de servidores:', font=my_font)
entrada1 = Entry(ventana)
label2 = Label(ventana, text='Consumo de potencia de servidores:', font=my_font)
entrada2 = Entry(ventana)
label3 = Label(ventana, text='Cantidad de horas:', font=my_font)
entrada3 = Entry(ventana)
label4 = Label(ventana, text='Tarifa de energía por KWh (kilovatios):', font=my_font)
entrada4 = Entry(ventana)
button1 = Button(ventana, text='Calcular', font=my_font)
button2 = Button(ventana, text='Borrar', font=my_font, command= borrar_datos)

# Posicionando los widgets
label1.grid(row=0, column=0, padx= 8, pady= 10, sticky='W')
entrada1.grid(row=0, column=1, padx= 8, pady= 10, sticky='W')
label2.grid(row=1, column=0, padx= 8, pady= 10, sticky='W')
entrada2.grid(row=1, column=1, padx= 8, pady= 10, sticky='W')
label3.grid(row=2, column=0, padx= 8, pady= 10, sticky='W')
entrada3.grid(row=2, column=1, padx= 8, pady= 10, sticky='W')
label4.grid(row=3, column=0, padx= 8, pady= 10, sticky='W')
entrada4.grid(row=3, column=1, padx= 8, pady= 10, sticky='W')
button1.grid(row=4, column=1, padx= 10, pady= 20)
button2.grid(row=4, column=0, padx= 10, pady= 20)

result_text = Text(ventana,height = 6,width = 52,bg="white",fg="black")
result_text.grid(row = 6,columnspan = 2)

# Función para calcular el costo total
def calcular_costo_total():
    cantidad_servidores = int(entrada1.get())
    consumo_potencia_servidores = float(entrada2.get())
    cantidad_horas = int(entrada3.get())
    tarifa_energia_kwh = float(entrada4.get())

    costo_total_por_hora = cantidad_servidores * consumo_potencia_servidores * cantidad_horas * tarifa_energia_kwh
    costo_total_por_dia = costo_total_por_hora * 24
    costo_total_por_mes = costo_total_por_dia * 30
    costo_total_por_anio = costo_total_por_mes * 12

    # Dar formato a los números en dolar
    costo_total_por_hora = locale.currency(costo_total_por_hora, grouping=True)
    costo_total_por_dia = locale.currency(costo_total_por_dia, grouping=True)
    costo_total_por_mes = locale.currency(costo_total_por_mes, grouping=True)
    costo_total_por_anio = locale.currency(costo_total_por_anio, grouping=True)

    # Insertar los resultados en el widget Text
    result_text.insert(END,f'Costo total por hora: '+ str(costo_total_por_hora) + '\n')
    result_text.insert(END,f'Costo total por día: '+ str(costo_total_por_dia) + '\n')
    result_text.insert(END,f'Costo total por mes: '+ str(costo_total_por_mes) + '\n')
    result_text.insert(END,f'Costo total por año: '+ str(costo_total_por_anio) + '\n')

# Asociar la función al botón
button1.config(command=calcular_costo_total)

# Iniciar la ventana principal
ventana.mainloop()
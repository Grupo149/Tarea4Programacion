import tkinter as tk
from tkinter import messagebox

from Cliente import registrar_cliente
from Servicios import ReservaSalas


# Registrar cliente
def registrar():

    nombre = entry_nombre.get()
    identificacion = entry_id.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()

    resultado = registrar_cliente(
        nombre,
        identificacion,
        correo,
        telefono
    )

    if resultado:

        messagebox.showinfo(
            "Registro",
            "Cliente registrado correctamente"
        )

    else:

        messagebox.showerror(
            "Error",
            "No se pudo registrar el cliente"
        )


# Calcular reserva
def calcular_reserva():

    try:

        horas = int(entry_horas.get())

        sala = ReservaSalas(
            costo_base=50000,
            horas=horas,
            tipo_sala="VIP"
        )

        costo = sala.calcular_costo()

        messagebox.showinfo(
            "Costo",
            f"Total reserva: ${costo}"
        )

    except:

        messagebox.showerror(
            "Error",
            "Ingrese un número válido"
        )


# Ventana principal
ventana = tk.Tk()

ventana.title("Sistema de Reservas")

ventana.geometry("400x500")


# Título
titulo = tk.Label(
    ventana,
    text="Sistema de Reservas",
    font=("Arial", 16)
)

titulo.pack(pady=10)


# Nombre
tk.Label(ventana, text="Nombre").pack()

entry_nombre = tk.Entry(ventana)

entry_nombre.pack()


# Identificación
tk.Label(ventana, text="Identificación").pack()

entry_id = tk.Entry(ventana)

entry_id.pack()


# Correo
tk.Label(ventana, text="Correo").pack()

entry_correo = tk.Entry(ventana)

entry_correo.pack()


# Teléfono
tk.Label(ventana, text="Teléfono").pack()

entry_telefono = tk.Entry(ventana)

entry_telefono.pack()


# Botón registrar
tk.Button(
    ventana,
    text="Registrar Cliente",
    command=registrar
).pack(pady=10)


# Horas reserva
tk.Label(
    ventana,
    text="Horas de reserva"
).pack()

entry_horas = tk.Entry(ventana)

entry_horas.pack()


# Botón calcular
tk.Button(
    ventana,
    text="Calcular Reserva VIP",
    command=calcular_reserva
).pack(pady=10)


# Ejecutar ventana
ventana.mainloop()



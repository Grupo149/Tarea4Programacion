# Importar herramientas para crear clases abstractas

from abc import ABC, abstractmethod

# Excepcion personalizada, sirve para mostrar errores con los clientes

class ClienteError(Exception):
    pass

#Clase abstracta persona

class Persona(ABC):

    # Constructor principal

    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.nombre = identificacion

# Metodo para clases hijas

@abstractmethod
def mostrar_informacion(self):
    pass

# Clase cliente hereda de Persona

class Cliente(Persona):

    # Constructor de cliente

    def __init__(self, nombre, identificacion, correo, telefono):

        # Validacion: nombre no puede estar vacio

        if nombre == "":
            raise ClienteError("Nombre Vacio")
        
        # Validacion: identificacion debe ser numerica

        if not identificacion.isdigit():
            raise ClienteError("Identificacion invalida")
        
        # Guardar correo y telefono

        self.correo = correo
        self.telefono = telefono

        # Metodo obligatorio heredado
        def mostrar_informacion(self):

            # Mostrar informacion completa del cliente
            print("Nombre:", self.nombre) 
            print("ID", self.identificacion)
            print("Correo", self.correo)
            print("Telefono", self.telefono)

# Lista de clientes

clientes =[]

# Funcion registar cliente

def registrar_cliente(nombre, identificacion, correo, telefono):

    try:
        # Crear nuevo cliente
        cliente = Cliente(nombre, identificacion, correo, telefono)
        clientes.append(cliente)
        print("Cliente registrado correctamente")

    except ClienteError as error:

        # Mostrar error sin detener el programa

        print("Error:", error)

#Pruebas

        # Cliente válido
if __name__ == "__main__":("Yeison","1105612218","yeisonq2000@gmail.com","3107396243")

# Cliente inválido
if __name__ == "__main__":("","abc","correo","123")
from abc import ABC, abstractmethod

# Excepción personalizada
class ClienteError(Exception):
    pass

# Clase abstracta Persona
class Persona(ABC):

    # Constructor
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    # Método abstracto
    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase Cliente
class Cliente(Persona):

    def __init__(self, nombre, identificacion, correo, telefono):

        # Validación nombre
        if nombre == "":
            raise ClienteError("El nombre no puede estar vacío")

        # Validación identificación
        if not identificacion.isdigit():
            raise ClienteError("La identificación debe ser numérica")

        # Heredar atributos
        super().__init__(nombre, identificacion)

        # Atributos propios
        self.correo = correo
        self.telefono = telefono

    # Método obligatorio heredado
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("ID:", self.identificacion)
        print("Correo:", self.correo)
        print("Teléfono:", self.telefono)


# Lista de clientes
clientes = []


# Función registrar cliente
def registrar_cliente(nombre, identificacion, correo, telefono):

    try:
        cliente = Cliente(
            nombre,
            identificacion,
            correo,
            telefono
        )

        clientes.append(cliente)

        print("Cliente registrado correctamente")

        return True

    except ClienteError as error:

        print("Error:", error)

        return False
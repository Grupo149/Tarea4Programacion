from abc import ABC, abstractmethod

# Clase abstracta principal
class Servicio(ABC):
    def __init__(self, nombre_servicio, costo_base):
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

# Tu implementación de Reserva de salas
class ReservaSalas(Servicio):
    def __init__(self, costo_base, horas, tipo_sala="Estándar"):
        super().__init__("Reserva de Salas", costo_base)
        self.horas = horas
        self.tipo_sala = tipo_sala

    def calcular_costo(self):
        factor = 1.20 if self.tipo_sala.upper() == "VIP" else 1.0
        return (self.costo_base * self.horas) * factor

# Tu implementación de Alquiler de equipos
class AlquilerEquipos(Servicio):
    def __init__(self, costo_base, cantidad, dias):
        super().__init__("Alquiler de Equipos", costo_base)
        self.cantidad = cantidad
        self.dias = dias

    def calcular_costo(self):
        total = self.costo_base * self.cantidad * self.dias
        if self.dias > 5:
            total *= 0.90
        return total

# Tu implementación de Asesorías especializadas
class AsesoriaEspecializada(Servicio):
    def __init__(self, costo_base, tema):
        super().__init__("Asesoría Especializada", costo_base)
        self.tema = tema

    def calcular_costo(self, es_urgente=False, descuento_estudiante=0):
        total = self.costo_base
        if es_urgente:
            total += 50000
        if descuento_estudiante > 0:
            total -= (total * (descuento_estudiante / 100))
        return total
    # --- BLOQUE DE PRUEBA ---
if __name__ == "__main__":
    print("Verificando cálculos de Yerly:")
    
    # Probar Reserva de Salas (VIP)
    sala_vip = ReservaSalas(costo_base=50000, horas=2, tipo_sala="VIP")
    print(f"- Costo Sala VIP (2h): ${sala_vip.calcular_costo()}")
    
    # Probar Alquiler de Equipos (con descuento por > 5 días)
    equipos = AlquilerEquipos(costo_base=10000, cantidad=1, dias=6)
    print(f"- Costo Alquiler (6 días): ${equipos.calcular_costo()}")
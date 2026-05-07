import Cliente
import Servicios

Cliente.registrar_cliente(
    "Yeison",
    "1105612218",
    "yeison@gmail.com",
    "3107396243"
)
sala = Servicios.ReservaSalas(
    costo_base=50000,
    horas=2,
    tipo_sala="VIP"
)

print("Costo sala:", sala.calcular_costo())



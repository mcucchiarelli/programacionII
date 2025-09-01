#Creamos la clase Vuelo (codigo, origen, destino, fecha, precio) Tareas 
# 1. Creá 6 vuelos con orígenes/destinos, fechas y precios distintos en una lista con un for 
# 2. Mostrá los códigos de los vuelos con origen EZE y precio < 200.000 pesos.

class Vuelo:
    def __init__(self, codigo: str, origen: str, destino: str, fecha: str, precio: float) -> None:
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio

# Datos de vuelos dados

datos_vuelos = [
    ("AR123", "EZE", "JFK", "2023-10-01", 150000.0),
    ("AA456", "EZE", "LAX", "2023-11-15", 250000.0),
    ("DL789", "EZE", "ORD", "2023-12-20", 180000.0),
    ("UA101", "AEP", "MIA", "2023-09-05", 220000.0),
    ("LA202", "EZE", "SCL", "2023-08-30", 120000.0),
    ("AF303", "EZE", "CDG", "2023-07-25", 300000.0)
]

# Crear lista de objetos Vuelo

vuelos = []
for codigo, origen, destino, fecha, precio in datos_vuelos:
    vuelo = Vuelo(codigo, origen, destino, fecha, precio)
    vuelos.append(vuelo)
            
# Mostrar códigos de vuelos con origen EZE y precio < 200000

print("Vuelos desde Ezeiza con precio menor a 200000 pesos:")
for v in vuelos:
    if v.origen == "EZE" and v.precio < 200000:
        print(v.codigo)
        
    



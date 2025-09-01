# PARA CALIFICAR: Estamos desarrollando un sistema para una aerolínea y definimos la clase Vuelo (codigo, origen, destino, fecha, precio). Tareas: 
#1. Cargar 6 vuelos en una lista, usamos la misma lista del ejercicio1_4.py 
#2. Construir una lista con los códigos de vuelos desde "EZE" y precio < 200000 usando for. 
#3. Encontrar el más barato hacia un destino dado (p. ej. "COR") con for (sin min). 
#4. Ajustar el precio de uno con set_precio y volver a calcular.

class Vuelo:
    def __init__(self, codigo, origen, destino, fecha, precio):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio

    #GET
    
    def get_codigo(self):
        return self.codigo

    def get_origen(self):
        return self.origen

    def get_destino(self):
        return self.destino

    def get_fecha(self):
        return self.fecha

    def get_precio(self):
        return self.precio

    #SET
    
    def set_codigo(self, nuevo_codigo: str) -> None:
        self.codigo = nuevo_codigo
    def set_origen(self, nuevo_origen: str) -> None:
        self.origen = nuevo_origen
    def set_destino(self, nuevo_destino: str) -> None:
        self.destino = nuevo_destino
    def set_fecha(self, nueva_fecha: str) -> None:
        self.fecha = nueva_fecha
    def set_precio(self, nuevo_precio: float) -> None:
        self.precio = nuevo_precio

#1. Cargar 6 vuelos en una lista, usamos la misma lista del ejercicio1_4.py

datos_vuelos = [
    ("AR123", "EZE", "JFK", "2023-10-01", 150000.0),
    ("AA456", "EZE", "LAX", "2023-11-15", 250000.0),
    ("DL789", "EZE", "ORD", "2023-12-20", 180000.0),
    ("UA101", "AEP", "MIA", "2023-09-05", 220000.0),
    ("LA202", "EZE", "SCL", "2023-08-30", 120000.0),
    ("AF303", "EZE", "CDG", "2023-07-25", 300000.0)
]
vuelos = []
for codigo, origen, destino, fecha, precio in datos_vuelos:
    vuelo = Vuelo(codigo, origen, destino, fecha, precio)
    vuelos.append(vuelo)

#2. Construir una lista con los códigos de vuelos desde "EZE" y precio < 200000 usando for.

vuelos_eze_baratos = []
for vuelo in vuelos:
    if vuelo.get_origen() == "EZE" and vuelo.get_precio() < 200000:
        vuelos_eze_baratos.append(vuelo.get_codigo())       
print("Códigos de vuelos desde EZE con precio < 200000:", vuelos_eze_baratos)

#3. Encontrar el más barato hacia un destino dado (p. ej. "COR") con for (sin min).

destino_buscado = "ORD"  
vuelo_mas_barato = None 
for vuelo in vuelos:
    if vuelo.get_destino() == destino_buscado:
        if vuelo_mas_barato is None or vuelo.get_precio() < vuelo_mas_barato.get_precio():
            vuelo_mas_barato = vuelo            
if vuelo_mas_barato:
    print(f"El vuelo más barato hacia {destino_buscado} es {vuelo_mas_barato.get_codigo()} con precio {vuelo_mas_barato.get_precio()}") 
else:
    print(f"No hay vuelos hacia {destino_buscado}")

#4. Ajustar el precio de uno con set_precio y volver a calcular.

for vuelo in vuelos:
    if vuelo.get_codigo() == "AA456":  #Ajustar precio del vuelo AA456
        vuelo.set_precio(180000.0)      #Nuevo precio   
        break

#Volver a calcular 

vuelos_eze_baratos = []  #Reiniciar lista
for vuelo in vuelos:
    if vuelo.get_origen() == "EZE" and vuelo.get_precio() < 200000:
        vuelos_eze_baratos.append(vuelo.get_codigo())   
print("Códigos de vuelos desde EZE con precio < 200000 después del ajuste:", vuelos_eze_baratos)    
#Recalcular vuelo más barato hacia COR
vuelo_mas_barato = None
for vuelo in vuelos:
    if vuelo.get_destino() == destino_buscado:
        if vuelo_mas_barato is None or vuelo.get_precio() < vuelo_mas_barato.get_precio():
            vuelo_mas_barato = vuelo
if vuelo_mas_barato:
    print(f"El vuelo más barato hacia {destino_buscado} después del ajuste es {vuelo_mas_barato.get_codigo()} con precio {vuelo_mas_barato.get_precio()}")  
else:
    print(f"No hay vuelos hacia {destino_buscado} después del ajuste")  


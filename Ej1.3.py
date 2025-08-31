#Crea una clase Dispositivo con los siguientes atributos: marca, modelo, anio, precio 
# 1. Creá 6 dispositivos con año y precio guardándolo en una lista 
# 2. Mostrá la lista de dispositivos con sus precios.

class Dispositivo:
    def __init__(self, marca: str, modelo: str, anio: int, precio: float) ->None:
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

d1 = Dispositivo("Apple", "iPhone 13", 2021, 999.99)
d2 = Dispositivo("Samsung", "Galaxy S21", 2021, 799.99)
d3 = Dispositivo("Google", "Pixel 6", 2021, 599.99)
d4 = Dispositivo("OnePlus", "9 Pro", 2021, 969.00)
d5 = Dispositivo("Sony", "Xperia 1 III", 2021, 1299.99) 
d6 = Dispositivo("Xiaomi", "Mi 11", 2021, 749.99)

dispositivos = [d1, d2, d3, d4, d5, d6]

for dispositivo in dispositivos:
    print(f"Marca: {dispositivo.marca}, Modelo: {dispositivo.modelo}, Año: {dispositivo.anio}, Precio: ${dispositivo.precio}")
        
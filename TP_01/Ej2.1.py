#Estamos desarrollando un sistema para un supermercado tenemos que definir la clase Articulo (nombre, precio, stock, categoría) 
#1. Crear una lista con 5 artículos. 
#2. Construir otra lista con los nombres de los artículos con precio > 4000 usando for y append. 
#3. Cambiar el precio de uno de ellos con set_precio y muestra el cambio. 


class Articulo:
    def __init__(self, nombre, precio, stock, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    #GET
    
    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_stock(self):
        return self.stock

    def get_categoria(self):
        return self.categoria

    #SET
    
    def set_nombre(self, nuevo_nombre: str) -> None:
        self.nombre = nuevo_nombre
    def set_precio(self, nuevo_precio: float) -> None:
        self.precio = nuevo_precio
    def set_stock(self, nuevo_stock: int) -> None:
        self.stock = nuevo_stock
    def set_categoria(self, nueva_categoria: str) -> None:
        self.categoria = nueva_categoria

#1. Crear una lista con 5 artículos.
articulos = [
    Articulo("Leche", 3500, 20, "Lácteos"),
    Articulo("Pan", 1500, 50, "Panadería"),
    Articulo("Queso", 4500, 15, "Lácteos"),
    Articulo("Carne", 8000, 10, "Carnicería"),
    Articulo("Manzanas", 3000, 30, "Frutas")
]

#2. Construir otra lista con los nombres de los artículos con precio > 4000 usando for y append.

caros = []
for articulo in articulos:
    if articulo.get_precio() > 4000:
        caros.append(articulo.get_nombre()) 
print("Artículos con precio > 4000:", caros)

#3. Cambiar el precio de uno de ellos con set_precio y mostrar el cambio.

print("Precio original de Queso:", articulos[2].get_precio()) #ver precio actual
articulos[2].set_precio(5000)       #cambiar precio 
print("Nuevo precio de Queso:", articulos[2].get_precio())  #ver nuevo precio


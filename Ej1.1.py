class Ciudad:
    def __init__(self, nombre: str, provincia: str, poblacion: int) -> None:
        self.nombre = nombre
        self.provincia = provincia
        self.poblacion = poblacion

# Instanciamos dos ciudades

ciudad1 =Ciudad("La Plata", "Buenos Aires", 8000000)
ciudad2 =Ciudad("Mar del Plata", "Buenos Aires", 6000000)
ciudad3 =Ciudad("Cordoba", "Cordoba", 4000000)

# Mostramos los atributos de cada ciudad

print(ciudad1.nombre, ciudad1.provincia, ciudad1.poblacion)
print(ciudad2.nombre, ciudad2.provincia, ciudad2.poblacion)
print(ciudad3.nombre, ciudad3.provincia, ciudad3.poblacion)
        
# Usamos vars() para ver el diccionario interno de cada ciudad

print(vars(ciudad1))
print(vars(ciudad2))
print(vars(ciudad3))


#prueba


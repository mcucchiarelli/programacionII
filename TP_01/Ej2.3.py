#Estamos desarrollando una plataforma de streaming con un servicio OTT de suscripción (cómo Netflix)  y queremos armar la clase Pelicula (titulo, director, duracion_min, genero) 
#1. Crear 5 películas. 
#2. Construir una lista con títulos del género "Drama" usando for. 
#3. Corregir la duración de una con set_duracion_min.

class Pelicula:
    def __init__(self, titulo, director, duracion_min, genero):
        self.titulo = titulo
        self.director = director
        self.duracion_min = duracion_min
        self.genero = genero

    #GET
    
    def get_titulo(self):
        return self.titulo

    def get_director(self):
        return self.director

    def get_duracion_min(self):
        return self.duracion_min

    def get_genero(self):
        return self.genero

    #SET
    
    def set_titulo(self, nuevo_titulo: str) -> None:
        self.titulo = nuevo_titulo
    def set_director(self, nuevo_director: str) -> None:
        self.director = nuevo_director
    def set_duracion_min(self, nueva_duracion_min: int) -> None:
        self.duracion_min = nueva_duracion_min
    def set_genero(self, nuevo_genero: str) -> None:
        self.genero = nuevo_genero

#1. Crear 5 películas.
peliculas = [
    Pelicula("El Padrino", "Francis Ford Coppola", 175, "Drama"),
    Pelicula("Inception", "Christopher Nolan", 148, "Ciencia Ficción"),
    Pelicula("La La Land", "Damien Chazelle", 128, "Musical"),
    Pelicula("Forrest Gump", "Robert Zemeckis", 142, "Drama"),
    Pelicula("The Dark Knight", "Christopher Nolan", 152, "Acción")
]

#2. Construir una lista con títulos del género "Drama" usando for.
dramas = []
for pelicula in peliculas:
    if pelicula.get_genero() == "Drama":
        dramas.append(pelicula.get_titulo())    
print("Películas del género Drama:", dramas)

#3. Corregir la duración de una con set_duracion_min.

print("Duración original de Inception:", peliculas[1].get_duracion_min()) #ver duración actual
peliculas[1].set_duracion_min(150)       #cambiar duración  
print("Nueva duración de Inception:", peliculas[1].get_duracion_min())  #ver nueva duración





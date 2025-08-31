#1. Definir la clase Cancion

class Cancion:
    def __init__(self, titulo: str, artista: str, duracion_seg: int, genero: str) ->None:
        self.titulo =titulo
        self.artirsta = artista
        self.duracion_seg = duracion_seg
        self.genero = genero

#2. Crear 5 canciones de géneros y duraciones variadas

c1 = Cancion("rock para el negro atila", "Los Redonditos de Ricota", 320, "Rock")
c2 = Cancion("Billie Jean", "Michael Jackson", 294, "Pop")
c3 = Cancion("Smells Like Teen Spirit", "Nirvana", 301, "Grunge")
c4 = Cancion("master of puppets", "Metallica", 515, "Metal")
c5 = Cancion("my friend", "Red Hot Chili Peppers", 269, "Rock")

#3. Crear una lista con las canciones

lista = [
    c1,
    c2,
    c3,
    c4,
    c5
]

for cancion in lista:
    if cancion.genero == "Rock":
        print(cancion.titulo)
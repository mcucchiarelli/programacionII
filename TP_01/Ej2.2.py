#Estamos desarrollando un sistema para la UTN y tenemos que definir la clase Estudiante (nombre, legajo, anio_ingreso, carrera). Tareas 
#1. Crear 6 estudiantes. 
#2. Construir una lista con los legajos de carrera "TUP" usando for. 
#3. Cambiar la carrera de un alumno con set_carrera y volver a calcular. 

class Estudiante:
    def __init__(self, nombre, legajo, anio_ingreso, carrera):
        self.nombre = nombre
        self.legajo = legajo
        self.anio_ingreso = anio_ingreso
        self.carrera = carrera

    #GET
    
    def get_nombre(self):
        return self.nombre

    def get_legajo(self):
        return self.legajo

    def get_anio_ingreso(self):
        return self.anio_ingreso

    def get_carrera(self):
        return self.carrera

    #SET
    
    def set_nombre(self, nuevo_nombre: str) -> None:
        self.nombre = nuevo_nombre
    def set_legajo(self, nuevo_legajo: int) -> None:
        self.legajo = nuevo_legajo
    def set_anio_ingreso(self, nuevo_anio_ingreso: int) -> None:
        self.anio_ingreso = nuevo_anio_ingreso
    def set_carrera(self, nueva_carrera: str) -> None:
        self.carrera = nueva_carrera

#1. Crear 6 estudiantes.
estudiantes = [
    Estudiante("Ana", 1234, 2020, "TUP"),
    Estudiante("Luis", 5678, 2019, "Licenciatura"),
    Estudiante("Marta", 9101, 2021, "TUP"),
    Estudiante("Carlos", 1121, 2018, "Ingeniería"),
    Estudiante("Sofía", 3141, 2020, "TUP"),
    Estudiante("Jorge", 5161, 2019, "Arquitectura")
]
#2. Construir una lista con los legajos de carrera "TUP" usando for.

tup_legajos = []
for estudiante in estudiantes:
    if estudiante.get_carrera() == "TUP":
        tup_legajos.append(estudiante.get_legajo()) 
print("Legajos de estudiantes en TUP:", tup_legajos)

#3. Cambiar la carrera de un alumno con set_carrera y volver a calcular.

estudiantes[1].set_carrera("TUP")  #Cambiar carrera de Luis a TUP

tup_legajos = []                    #Reiniciar lista
for estudiante in estudiantes:      #Volver a calcular  
    if estudiante.get_carrera() == "TUP":
        tup_legajos.append(estudiante.get_legajo())
print("Legajos de estudiantes en TUP después del cambio:", tup_legajos)

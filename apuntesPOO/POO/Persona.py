# PROGRAMACIÓN ORIENTADA A OBJETOS

"""
- ABSTRACCIÓN: es la manera en que plasmamos las caracteristicas y comportamiento de un onjeto en una clase,
en un contexto especificos.

-HERENCÍA: es la capacidad de la clase de pasar atributos y/o comportamientos a otra clase u objeto.

"""

class Persona:

    compañia = "bancolombia"

    def __init__(self, id, nombre, correo, contrasena):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def verPersona(self):
        print(f"Id: {self.id}")
        print(f"nombre: {self.nombre}")
        print(f"correo: {self.correo}")
        print(f"compañia: {self.compañia}")
       
maria = Persona(1, "Maria", "mt@gmail.com", "mar123")
sebas = Persona(2, "sebas", "sb@gmail.com", "seb123")

maria.verPersona()
print("-----------------------------")
sebas.verPersona()

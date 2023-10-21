from apuntesPOO.POO.persona import Persona


class Estudiante(Persona):

    def __init__(self, id, nombre, correo, contrasena, programa, semestre):
        super().__init__(id, nombre, correo, contrasena)
        self.programa = programa
        self.semestre = semestre

    def verPersona(self):
            print(f"Id: {self.id}")
            print(f"nombre: {self.nombre}")
            print(f"correo: {self.correo}")
            print(f"compañia: {self.compañia}")
            print(f"programa: {self.programa}")

if __name__ == '__main__':
    estudiante1 = Estudiante(1,"maria","mail.com","mar123","desarrollo",1)
    print(estudiante1.programa)
    estudiante1.verPersona()
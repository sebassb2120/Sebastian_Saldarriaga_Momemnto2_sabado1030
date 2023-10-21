


from apuntesPOO.POO.Persona import Persona


class Profesor(Persona):

    def __init__(self, id, nombre, correo, contrasena, programa):
        super().__init__(id, nombre, correo, contrasena)
        self.programa = programa
       

    def verProfesor(self):
            print(f"Id: {self.id}")
            print(f"nombre: {self.nombre}")
            print(f"correo: {self.correo}")
            print(f"compañia: {self.compañia}")
            print(f"programa: {self.programa}")

if __name__ == '__main__':
    Profesor1 = Profesor(1,"jose","jose@gmail.com","jose123","desarrollo")
    print(Profesor1.programa)
    Profesor1.verProfesor()
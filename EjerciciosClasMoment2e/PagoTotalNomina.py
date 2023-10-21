def datosPersonal(trabajadores, id, nombre, apellido, cargo, area, salario):

    trabajador = {
    "id":id,
    "nombre": nombre,
    "apellido": apellido,
    "cargo" : cargo,
    "area": area,
    "salario":salario
    }

    if salario <= 2200000:
        salario + 160000

    trabajadores[id]=trabajador
    print(f"el trabajador fue registrado con exito")

def colillaPago(trabajadores, id):
    if id in trabajadores:
        trabajador = trabajadores[id]
        print(f"ID: {trabajador['id']}")
        print(f"nombre: {trabajador['nombre']}")
        print(f"apellido: {trabajador['apellido']}")
        print(f"cargo: {trabajador['cargo']}")
        print(f"area: {trabajador['area']}")
        print(f"salario: {trabajador['salario']}") 
    
    else:
        print("El trabajador no  ha sido previamente registrado")

# Guardar lista de trabajadores enb diccionario
trabajadores = {}

while True:
    print("Elige tu Usuario")
    print("1. INGRESAR DATOS EMPLEADO")
    print("2. EMPLEADO")
    print("3. ANALISTA")
    print("4. SALIR")
    
    usuario = input("Ingresa opcion seleccionada: ")

    print("-------------------------------------------------------------------------")

    if usuario == "1":
        id = input("Agrueda id del empleado: ")
        nombre = input("Agrega el nombre del empleado: ")
        apellido = input("Agrega el apellido del empleado: ")
        cargo = input("Agrega el cargo del empleado: ")
        area = input("Agrega el area del empleado: ")
        salario = float(input("Agrega el salario del empleado: "))

        datosPersonal(trabajadores, id, nombre, apellido, cargo, area, salario)

        print("-------------------------------------------------------------------------")
    
    
    elif usuario == "2":
        print("DOMINIO EMPLEADO")
        print("Favaor ingresa tus datos para iniciar busqueda")
        id = input("Ingresa la cedula: ")
        colillaPago(trabajadores,id)

        print("-------------------------------------------------------------------------")


    elif usuario == "3":
        print("1. Buscar por empleado")
        print("2. ver todos los empleados")

        opcion = input("Elija una opción: ")
        if opcion == "1":
            print("Ingreda el ID del empleado")
            id = input("id = ")
            colillaPago(trabajadores, id)
        
        elif opcion == "2":
            print("COLILLA DE PAGO DE TODOS LOS EMPLEADOS")
            for i in trabajadores.values():
                print(i)

        
        else:
            print("opcion no valida ")

    elif usuario == "4":
        break

  




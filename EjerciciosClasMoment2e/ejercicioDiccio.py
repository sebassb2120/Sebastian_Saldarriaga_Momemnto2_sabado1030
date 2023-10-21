## Ejercicio usando dicccionario y funciones en el que creemos un producto
## Con las siguientes claves:
## id, nombre, costo, cantidad, margendeganancia
## Se deben almacenar los productos con dos campos adicionales calculados
## precioventa = costo/(1-margenganancia) y valor de inventarios = cantidad * costo



def agregarProducto(productos,id,nombre, costo, cantidad, margendeganancia):
    precioventa = costo / (1 - margendeganancia)
    valorInventario = cantidad * costo

    producto={
        'id': id,
        'nombre': nombre,
        'costo': costo,
        'cantidad': cantidad,
        'margendeganancia': margendeganancia,
        'precioventa': precioventa,
        'valorinventarios': valorInventario
    }
    productos[id] = producto
    print(f"producto {nombre} agregado con exito")

def mostrar_producto(productos, id):
    if id in productos:
        producto = productos[id]
        print(f"ID: {producto['id']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Costo: {producto['costo']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Margen de Ganancia: {producto['margendeganancia']}")
        print(f"Precio de Venta: {producto['precioventa']}")
        print(f"Valor de Inventario: {producto['valorinventarios']}")
    else:
        print("El producto no fue registrado.")

#Guardar productos
productos = {}

while True:
        print("n\ ---SUPER MERCADO---")
        print("1. AGREGAR PRODUCTO")
        print("2. CONSULTAR PRODUCTO")
        print("3. SALIR DE LA TIENDA")

        opcion = input("Seleccione una opcion: ")
    
        if opcion == "1":
            id = input("AGREGUE UN ID:")
            nombre = input("AGREGUE UN nombre del producto:")
            costo = float(input("AGREGUE costo:"))
            cantidad = int(input("AGREGUE cantidad:"))
            margendeganancia = float(input("AGREGUE UN margen de ganancia:")) / 100

            agregarProducto(productos,id,nombre, costo, cantidad, margendeganancia)

        elif opcion == "2":
            id = input("ingrese el id del producto que deseas consulat: ")
            mostrar_producto(productos,id)
        
        elif opcion == "3":
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")  

        



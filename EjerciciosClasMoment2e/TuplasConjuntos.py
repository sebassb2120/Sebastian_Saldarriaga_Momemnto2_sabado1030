print("______________________________tuplas________________________")

my_tuple = (19, 1.75, "sebastian", "saldarriaga")

### mirar cuantos elementos existen llamados igual ### sirve para las listas y tuplas
print(my_tuple.count("sebastian"))

### mirar el indice ###
print(my_tuple.index("sebastian"))

## buscar tuplas ###
print (my_tuple[1:3])

#Concatenar tuplas:
my_tuple_two = ("medellin", "girardota", "programacion")
concatenacio = my_tuple + my_tuple_two
print(concatenacio)

#Contar elementos:
conteo_elementos = my_tuple.count(19)
print(conteo_elementos)

#Comprobar si un elemento está en la tupla: 
comprobar = "sebastian" in my_tuple
print(comprobar)

colores = ("amariilo", "azul", "rojo")
print(type(colores))
print(len(colores))
print(colores[0])

coloresList = list(colores)
print(coloresList)
print(type(coloresList))

coloresList.append("verde")
print(coloresList)

colores = tuple(coloresList)
print(type(colores))
print(colores)


for i in range(len(colores)):
    print(colores[i])

print(colores[0:2])

print("______________________________conjuntos________________________")

usuarios = {"user1", "user2", "use3", "user4"}

print("_________________")
#agregar usuarios
usuarios.add("user5")
print(usuarios)


print("_________________")
#para mirar si hay algun elemento en el conjunto
print("user2" in usuarios)
print("hola" in usuarios)


print("_________________")
#remover elemento
usuarios.remove("user4")
print(usuarios)

for i in usuarios:
    print(i)


print("_________________")

usuarios = frozenset(["numero1","numero2"])

usuarios2 = {usuarios, "numero3", "numero4"}

print(usuarios2)

print("_________________")
##Se pueden unir conjuntos con datos repetidos usando update
conjuntoUno = {"sebas", "camilo", "mora","cordoba"}
conjuntoDos = {"santi","camilo", "puga", "sebas"}

conjuntoUno.update(conjuntoDos)

for i in conjuntoUno:
    print(i)
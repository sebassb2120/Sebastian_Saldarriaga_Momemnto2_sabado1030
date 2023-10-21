#las tuplas se encierran en parentesis y son inmutables

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
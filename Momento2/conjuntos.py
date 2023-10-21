# los conjuntos son inmodificables
# son ordenados
# no permite duplicados
# son iterables
# se construye usando {}
# permite agregar o eliminar items

usuarios = {"user1", "user2", "use3", "user4"}

#usuarios[1] =usuarioNan  esto no se puede hacer

#agregar usuarios
usuarios.add("user5")
print(usuarios)

#para mirar si hay algun elemento en el conjunto
print("user2" in usuarios)
print("hola" in usuarios)

#remover elemento
usuarios.remove("user4")
print(usuarios)

for i in usuarios:
    print(i)


print("_________________")

usuarios = frozenset(["numero1","numero2"])

usuarios2 = {usuarios, "numero3", "numero4"}

print(usuarios2)
print("MENU")
print("1 --> Menu Principal")
print("2 --> Menu Usuario")
print("3 --> Menu Compras \n")

entrada = int(input("Ingrese un valor: "))


if entrada == 1:
    print("Menu principal")
elif entrada == 2:
    print("Menu usuario")
elif entrada == 3:
    print("Menu compras")
else:
    print("No se ha seleccionado ninguna opcion valida")



print("Ingrese sus 5 notas:")
while True:
    while True:
        try:
            nota_1 = int(input("Nota 1°: "))
            break
        except ValueError:
            print("Ingrese un valor numérico que no sea decimal")

    while True:
        try:
            nota_2 = int(input("Nota 2°: "))
            break
        except ValueError:
            print("Ingrese un valor numérico que no sea decimal")

    while True:
        try:
            nota_3 = int(input("Nota 3°: "))
            break
        except ValueError:
            print("Ingrese un valor numérico que no sea decimal")       

    while True:
        try:
            nota_4 = int(input("Nota 4°: "))
            break
        except ValueError:
            print("Ingrese un valor numérico que no sea decimal")

    while True:
        try:
            nota_5 = int(input("Nota 5°: "))
            break
        except ValueError:
            print("Ingrese un valor numérico que no sea decimal")
    break

Lista_notas = [nota_1, nota_2, nota_3, nota_4, nota_5]
nota_max=max(Lista_notas)
nota_min=min(Lista_notas)
promedio= sum(Lista_notas) / len(Lista_notas)

print(f"Sus notas son: {Lista_notas}")
print(f"Su nota mas alta es: {nota_max}")
print(f"Su nota mas baja es: {nota_min}")
print(f"SU promedio final es: {promedio}")









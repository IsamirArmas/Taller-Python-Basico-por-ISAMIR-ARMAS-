import random

lista = ["python", "programacion", "taller", "usac", "minecraft", "fortnite", "isamir"]
palaba_secreta = random.choice(lista)

intentos = 10
letra_adivinadas = []

print("========================================")
print("             Adivina la palabra         ")
print("========================================")
print("Tienes", intentos, "Oportunidades")


while intentos > 0:
    mostrar_palabra = ""
    todas_adivinadas = True  

    for letra in palaba_secreta:

        if letra in letra_adivinadas:
            mostrar_palabra += letra + " "
        else:
            mostrar_palabra += "_ "
            todas_adivinadas = False

    print("PALABRA : " ,mostrar_palabra)

    if todas_adivinadas:
        print("Felicidades adivinaste la palabra: ", palaba_secreta.upper())
        break

    print("intentos restantes", intentos)

    intento = input("Ingresa una letra: ").lower()
    # len()
    #isalpha()  devolver true si lo que esta adentro es una letra
    if len(intento) != 1 or not intento.isalpha():
        print("Ingresa solamente 1 letra: ")
        continue
    
    #append agrega la variable a la lista especificada
    letra_adivinadas.append(intento)

    if intento not in palaba_secreta:
        intentos = intentos - 1
        print("La letra", intento, "No esta en la palabra")
    else:
        print("La letra", intento, "Si esta en la palabra")

if intentos == 0:
    print("HAS PERDIDO   Se acabaron tu intentos ")
    print("La palabra secreta era", palaba_secreta.upper())
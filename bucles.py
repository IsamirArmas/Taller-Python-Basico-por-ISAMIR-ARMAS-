#Funcion range
range(5)  # 0 1 2  3 4 

#For

"""for numero in range(5):
    print("Esta es la sentencia", numero)

for letra in "Hola Mundo":
    print(letra)

lista = ["Isamir ", "Wilver", "Jaime"]

for nombre in lista:
    print("Hola ", nombre)"""


#While
while True:
    print("Hola Mundo")

    break


while True:
    entrada = input("Ingresa un comando: ")

    if entrada == "salir":
        print("Has salido del programa")
        break

    print("Comando ingresado ", entrada.upper()) #TODO En mayuscula
    print("Comando ingresado ", entrada.lower()) #TODO En minuscula
    


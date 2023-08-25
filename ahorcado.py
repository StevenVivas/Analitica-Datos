import random


palabras = ['computador', 'mouse', 'televisor']
palabra_random = random.choice(palabras)
intentos_maximos = 5


palabra_adivinar = ["_" for _ in palabra_random]


print(f"La palabra a adivinar es: {palabra_random}")
print(" ".join(palabra_adivinar))


vidas_restantes = intentos_maximos
letras_adivinadas = []


while vidas_restantes > 0 and "_" in palabra_adivinar:
    letra = input("Ingrese una letra: ")


    if len(letra) != 1:
        print("Por favor, ingrese una sola letra.")
        continue


    if letra in letras_adivinadas:
        print("Ya has adivinado esta letra antes.")
        continue
   
    letras_adivinadas.append(letra)


    aciertos = False
    for i in range(len(palabra_random)):
        if palabra_random[i] == letra:
            palabra_adivinar[i] = letra
            aciertos = True


    print(" ".join(palabra_adivinar))


    if not aciertos:
        vidas_restantes -= 1
        print(f"Letra incorrecta. Te quedan {vidas_restantes} vidas.")


if "_" not in palabra_adivinar:
    print(f"¡Has completado la palabra! Era: {palabra_random}")
elif vidas_restantes == 0:
    print(f"Se te acabaron las vidas. La palabra era: {palabra_random}")


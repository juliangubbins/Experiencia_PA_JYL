import random
def adivinar_numero():
    numero_jugador = int(input("Adivina buen adivinador... ¿Cuál es mi número entre 1 y 10? "))
    numero = random.randint(1,10)
    numero = int(numero)
    if numero_jugador == numero:
        print("¡Felicitaciones! Adivinaste")
    else:
        print(f"No adivinaste, sigue intentando. Mi número era: {numero}")
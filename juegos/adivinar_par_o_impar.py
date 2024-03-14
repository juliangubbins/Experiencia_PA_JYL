import random
def adivinar_par_o_impar():
    jugador = input("Par o impar: ").lower()
    numero = random.randint(1, 100)
    if numero % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
    if paridad == "par" and jugador == "par":
        print(f"Adivinaste, mi número era par: Número: {numero}")
    elif paridad == "impar" and jugador == "impar":
        print(f"Adivinaste, mi número era impar: Número: {numero}")
    else:
        print(f"No adivinaste, mi número era {numero}")
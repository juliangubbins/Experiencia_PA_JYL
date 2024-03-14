def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    import random

    pc = random.randint(1, 3)

    while True:

        jugador1 = input('Elige piedra, papel, o tijera: ')
        final = jugador1
        if jugador1.lower() == 'piedra':
            jugador1 = 1
            break
        elif jugador1.lower() == 'tijera':
            jugador1 = 2
            break
        elif jugador1.lower() == 'papel':
            jugador1 = 3
            break
        else:
            print("Selecciona una opcion valida")

    if pc == 1:
        finalpc = 'Piedra'
    elif pc == 2:
        finalpc = 'Tijera'
    else:
        finalpc = 'Papel'

    if jugador1 - pc == 0:
        print('Empate!')
    elif jugador1 - pc == 1:
        print('Perdiste :(')
    elif jugador1 - pc == -2:
        print('Perdiste :(')
    else:
        print('Ganaste!')

    print(f'Tu opcion: {final.lower()}\nPc: {finalpc.lower()}')
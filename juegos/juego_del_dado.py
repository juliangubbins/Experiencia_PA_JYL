def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """

    import random
    puntaje_usuario = 0
    puntaje_pc = 0

    while True:

        usuario = input('Presiona Enter para lanzar un dado')
        usuario = random.randint(1, 6)
        pc = random.randint(1, 6)

        puntaje_usuario += usuario
        puntaje_pc += pc
        print(f'Puntuacion Usuario: {puntaje_usuario}\nPuntaje Pc: {puntaje_pc}')

        if puntaje_usuario >= 30 and puntaje_usuario > puntaje_pc:
            print(f'Ganaste!\nPuntuacion Usuario: {puntaje_usuario}\nPuntaje Pc: {puntaje_pc}')
            break
        elif puntaje_pc >= 30 and puntaje_pc > puntaje_usuario:
            print(f'Perdiste :(\nPuntuacion Usuario: {puntaje_usuario}\nPuntaje Pc: {puntaje_pc}')
            break
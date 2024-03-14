def memoria(): 
    """ 
    Esta función representa el juego de memoria. 
    Debes generar una secuencia de números al azar y mostrarla al usuario. 
    Luego, debes pedir al usuario que repita la secuencia. 
    Se debe mostrar un mensaje si el usuario acierta o no. 
    """ 
     
    import random 
    import time 
 
    numero = random.randint(1000000, 9999999) 
    print(f'Secuencia: {numero}') 
 
    for i in range(5): 
        time.sleep(1) 
        print(5 - i) 
 
    for i in range(20): 
        print('XXXXXXXXXXXXXXXXXX') 
 
    final = int(input('Introduce la secuencia: ')) 
    if final == numero: 
        print('Ganaste!') 
    else: 
        print('Perdiste :(')
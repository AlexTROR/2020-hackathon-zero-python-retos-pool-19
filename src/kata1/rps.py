from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    
    player = player.lower()
    player = player.capitalize()

    ai = ai.lower()
    ai = ai.capitalize()

    # CASO USUARIO PIEDRA
    if player == options[0]:
        
        # CASO AI PIEDRA
        if ai == options[0]:
            return 'Empate!'

        #CASO AI PAPEL
        elif ai == options[1]:
            return 'Perdiste!'

        #CASO AI TIJERA
        else:
            return 'Ganaste!'


    # CASO USUARIO PAPEL
    if player == options[1]:
        
        # CASO AI PIEDRA
        if ai == options[0]:
            return 'Ganaste!'

        #CASO AI PAPEL
        elif ai == options[1]:
            return 'Empate!'

        #CASO AI TIJERA
        else:
            return 'Perdiste!'
    

    # CASO USUARIO TIJERA
    if player == options[2]:
        
        # CASO AI PIEDRA
        if ai == options[0]:
            return 'Perdiste!'

        #CASO AI PAPEL
        elif ai == options[1]:
            return 'Ganaste!'

        #CASO AI TIJERA
        else:
            return 'Empate!'
        

# Entry Point
def Game():
    
    ai = random.randint(0,2)
    ai = options[ai]

    player = input("Introduzca que quiere jugar (piedra, papel, tijera): ")

    winner = quienGana(player, ai)

    print(winner)


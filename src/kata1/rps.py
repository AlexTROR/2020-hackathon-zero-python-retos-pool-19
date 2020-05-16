from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    
    # CASO USUARIO PIEDRA
    if options[player] == options[0]:
        
        # CASO AI PIEDRA
        if options[ai] == options[0]:
            return 'Empate!'

        #CASO AI PAPEL
        elif options[ai] == options[1]:
            return 'Perdiste!'

        #CASO AI TIJERA
        else:
            return 'Ganaste!'


    # CASO USUARIO PAPEL
    if options[player] == options[1]:
        
        # CASO AI PIEDRA
        if options[ai] == options[0]:
            return 'Ganaste!'

        #CASO AI PAPEL
        elif options[ai] == options[1]:
            return 'Empate!'

        #CASO AI TIJERA
        else:
            return 'Perdiste!'
    

    # CASO USUARIO TIJERA
    if options[player] == options[2]:
        
        # CASO AI PIEDRA
        if options[ai] == options[0]:
            return 'Perdiste!'

        #CASO AI PAPEL
        elif options[ai] == options[1]:
            return 'Ganaste!'

        #CASO AI TIJERA
        else:
            return 'Empate!'
        

# Entry Point
def Game():

    player = input('Introduce el número que quieras jugar (0.PIEDRA, 1.PAPEL, 2.TIJERA): ')

    ai = random.randint(0, 3)
    
    winner = quienGana(player, ai)

    print(winner)


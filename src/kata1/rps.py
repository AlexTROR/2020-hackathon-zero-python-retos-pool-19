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

    if player == ai:
        return 'Empate!'

    # CASO USUARIO PIEDRA
    if player == options[0]:
        
        # CASO AI TIJERA
        if ai == options[2]:
            return 'Ganaste!'

        #CASO AI PAPEL
        elif ai == options[1]:
            return 'Perdiste!'



    # CASO USUARIO PAPEL
    if player == options[1]:
        
        # CASO AI PIEDRA
        if ai == options[0]:
            return 'Ganaste!'

        #CASO AI TIJERA
        elif ai == options[2]:
            return 'Perdiste!'

    

    # CASO USUARIO TIJERA
    if player == options[2]:
        
        # CASO AI PIEDRA
        if ai == options[0]:
            return 'Perdiste!'

        #CASO AI PAPEL
        elif ai == options[1]:
            return 'Ganaste!'

        

# Entry Point
def Game():
    
    ai = randint(0,2)
    ai = options[ai]

    player = input("Introduzca que quiere jugar (piedra, papel, tijera): ")

    print("La IA juega: " + ai)

    winner = quienGana(player, ai)

    print(winner)

#Game()

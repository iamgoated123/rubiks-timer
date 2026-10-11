import random

def scramblegen(length=20):
    moves=['F','R','L','U','D','B']
    mods=["","'","2"]
    scramble=[]
    last_move=""
    while len(scramble)<length:
        current_move=random.choice(moves)
        if current_move != last_move:
            current_mods=random.choice(mods)
            scramble.append(current_move+current_mods)
            last_move=current_move

    return " ".join(scramble)

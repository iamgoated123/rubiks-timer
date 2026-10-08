import random

def scramblegen(length=20):
    moves=['F','R','L','U','D','B']
    mods=["","'","2"]
    scramble=[]
    z=""
    while len(scramble)<length:
        x=random.choice(moves)
        if x != z:
            y=random.choice(mods)
            scramble.append(x+y)
            z=x

    return " ".join(scramble)

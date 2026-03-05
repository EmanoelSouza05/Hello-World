
def par(*args):
    pares = []
    for x in args:
        if x % 2 == 0:
            pares.append(x)
    return pares

def ecriture_binaire_entier_positif(dec):
    """ int -> bin
        passe un decimal en binaire 
    """
    binaire = ""
    while dec != 0:
        binaire += str(dec%2)
        dec = dec//2
    binaire = int(binaire[::-1])#reverse la chaine de caractere
    return binaire
"""
ALTERNATIVE ! 
binaire = [elm for elm in binaire]
    binaire = [binaire[(len(binaire)-1) - i ] for i in range(len(binaire))]
    binaire = "".join(binaire)
"""




def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = ... 
    tab[i] = ... 
    tab[j] = ... 

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(...): 
        for j in range(...): 
            if ... > ...: 
                echange(tab, j, ...) 



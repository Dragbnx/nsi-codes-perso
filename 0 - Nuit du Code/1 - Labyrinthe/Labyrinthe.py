import pyxel
import random

BLOC = 8
HAUT, BAS, GAUCHE, DROITE = (0, -BLOC), (0, BLOC), (-BLOC, 0), (BLOC, 0)



class Labyrinthe:
    """Représente un labyrinthe"""

    def __init__(self, n, m):
        self.dim = n, m
        self.murs = [[0 for j in range(m)]
                    for i in range(n)]
        self.generer()

    def est_dans(self, bloc):
        """ Labyrinthe, (int, int) -> bool
        Détermine si bloc est un indice de bloc valide pour le labyrinthe self """
        n, m = self.dim
        x, y = bloc
        return 0<=x<n and 0<=y<m

    def est_sol(self, bloc):
        """ Labyrinthe, (int, int) -> bool
        Détermine si bloc est un indice de bloc valide correspondant à un sol dans le labyrinthe self """
        x,y = bloc
        return self.murs[x][y] != 0

    def arrive(self, bloc):
        x,y = bloc
        return self.murs[x][y] == 2

    def blocs_possibles(self, position, visites):
        """ Labyrinthe, (int, int), {(int, int)} -> [(int, int)]
        Renvoie la liste des blocs voisins et non visités """
        liste = []
        x,y = position
        possibles =[(x, y-2), (x, y+2), (x-2, y), (x+2, y)]
        for elm in possibles:
            if self.est_dans(elm) and self.est_sol(elm) and not elm in visites:
                liste.append(elm)
        return liste

    def liste_sol(self):
        sol = []
        n, m = self.dim
        for i in range(n):
            for j in range(m):
                if self.murs[i][j]==1:
                    sol.append((i,j))
        return sol


    def generer(self):
        """ Labyrinthe
        Génère un labyrinthe de manière aléatoire """
        n, m = self.dim
        for i in range(n):
            for j in range(m):
                if i%2 == 1 and j%2 == 1:
                    self.murs[i][j] = 1
        visites = set()
        chemin = []
        position_courantes = (1,1)
        visites.add(position_courantes)
        chemin.append(position_courantes)
        while chemin != []:
            choix = self.blocs_possibles(position_courantes, visites)
            if choix == []:
                chemin.pop()
                if chemin!= []:
                    position_courantes = chemin[-1]
                continue
            nouvelle_position = random.choice(choix)
            x, y = position_courantes
            x1, y1 = nouvelle_position
            self.murs[(x+x1)//2][(y+y1)//2] = 1
            position_courantes = nouvelle_position
            visites.add(position_courantes)
            chemin.append(position_courantes)
        self.murs[n-2][m-2] = 2




    def afficher(self):
        """ Labyrinthe -> None
        Affiche le labyrinthe self à l'écran """
        n,m = self.dim
        for i in range(n):
            for j in range(m):
                pyxel.rect(i*8, j*8, 8,8,self.murs[i][j])




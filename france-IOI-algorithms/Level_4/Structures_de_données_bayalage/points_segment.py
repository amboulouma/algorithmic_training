# Étant donné N points sur une droite, combien de points au maximum peut-on couvrir à l'aide d'un intervalle de largeur L donnée ?

# Remarque: un point qui tombe pile au bord de l'intervalle est considéré comme couvert.

# CONSTRAINTS
# 1 <= N <= 100 000, où N est le nombre de points.
# 0 <= X <= 108, où X est l'abscisse d'un point.
# 0 <= L <= 108, où L est la largeur de l'intervalle.

# INPUT
# Sur la première ligne, deux entiers séparés par un espace: L puis N.
# La seconde ligne contient N entiers séparés par des espaces: les abscisses des points.
# OUTPUT
# Affichez simplement un entier: le nombre maximum de points que l'on peut couvrir avec un intervalle de la largeur donnée.

# EXAMPLE
# input:

# 4 9 -> 9 points sur un intervalle de largeur 4
# 1 4 6 8 9 13 15 16 18 -> Abscisses des points
# output:

# 3 -> 4,6,8
#      13,15,16


def getUpperBound(tab, uB):
    if uB in tab:
        return uB
    elif max(tab) > uB:
        for i in range(len(tab)):
            if tab[i] < uB:
                pass
            else:
                return tab[i-1]
    else:
        return max(tab)


L, N = map(int, input().split())
X = list(map(int, input().split()))
maxi = 0
for i in range(len(X)):
    upperBound = getUpperBound(X, X[i]+L)
    if len(X[i:X.index(upperBound)+1]) > maxi:
        maxi = len(X[i:X.index(upperBound)+1])
print(maxi)


# CONSTRAINTS
# 2 <= L, C <= 20, où L et C sont le nombre de lignes et de colonnes du labyrinthe.
# INPUT
# La première ligne de l'entrée contient deux entiers, L et C, séparés par un espace: le nombre de lignes et de colonnes du labyrinthe.

# Chacune des L lignes suivantes contient C caractères valant '#' ou '.', et décrivant une ligne du labyrinthe: '#' représente une case contenant un arbuste, et '.' représente une case libre.

# OUTPUT
# Vous devez écrire une ligne sur la sortie, contenant un entier: le nombre de manières différentes d'atteindre la sortie, sans repasser deux fois par la même case.

# EXAMPLE
# input:

# 10 10
# ##########
# .........#
# ###..#.#.#
# #.###...##
# #.#...#..#
# #...####.#
# #.#.....##
# #..#..#..#
# #...#..#.#
# ########.#
# output:

# 4


L, C = map(int, input().split())
labyrinthe = [0]*L*C
j = 0
for i in range(L):
    ligne = input()
    for c in ligne:
        if c == ".":
            labyrinthe[j] = 1
        j += 1

for j in range(C*L):
    if j == 0 or j == C-1 or j == L*C-1 or j == L*C-C+1:
        # 2 possibilities
    if 


print(labyrinthe)
    
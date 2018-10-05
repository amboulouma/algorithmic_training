# Problem and draft

# 0 <= N <= 100 000, le nombre de jours où le parc a reçu des visiteurs
# 0 <= V <= 10 000, le nombre maximum de visiteurs chaque jour
# 0 <= R <= 100 000, le nombre de périodes pour lesquelles il faut calculer le nombre de visiteurs

# INPUT
# La première ligne contient deux entiers: N et R

# La seconde ligne contient N entiers: le nombre de visiteurs pour chacun des N jours

# Les R lignes suivantes contiennent chacune deux entiers 1 <= D <= F <= N, les jours de début et de fin de la période

# OUTPUT
# Pour chaque période(D, F), vous devez écrire un entier: le nombre de visiteurs venus dans le parc entre les jours D(inclus) et F(inclus).

#     10 3
#     77 60 67 67 63 100 68 55 98 66
#     # 0  1  2  3  4  5  6  7  8  9
#     2 2 -> 60 = visiteurs[1]
#     1 10 -> 721 = sum(visiteurs[0 -> 9])
#     5 7 -> 231 = visiteur[4] + visiteur[5] + visiteur[6]


N, R = map(int, input().split())
V = list(map(int, input().split()))
for j in range(R):
    D, F = map(int, input().split())
    if D == F:
        print(V[D-1])
    else:
        s = 0
        n = F-D+1
        for i in range(n):
            s += V[D-1]
            D += 1
        print(s)

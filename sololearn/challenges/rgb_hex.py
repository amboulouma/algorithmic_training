# Challenge Rgb to hex
# Author Amine M Boulouma
# 23/03/2018
hexa = [""] * 3
hexa[0], hexa[1], hexa[2] = map(hex, map(int, input().split(' ')))
print(hexa)
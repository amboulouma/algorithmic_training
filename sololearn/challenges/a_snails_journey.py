# Challenge A Snail's Day
# Author Amine M Boulouma
# 23/03/2018
import math

h, a, b = map(float, input().split(' '))
print(str(math.ceil(h/(a-b))) + ' Days')
# Challenge Base converter
# Author Amine M Boulouma
# 23/03/2018
n, b = map(int, input().split(' '))
s = ''
while n >= b:
    s += str(int(n%b))
    n /= b 
s += str(int(n))
print(s[::-1])
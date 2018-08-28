n = int(input())
code_pos = list(map(int, input().split()))
r = int(input())
codes = list(map(int, input().split()))

containers = []

for i in range(n):
    if i + 1 not in code_pos:
        containers.add(code_pos[i])

for i in range(r):
    print()

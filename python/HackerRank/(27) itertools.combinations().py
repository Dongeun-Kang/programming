from itertools import combinations

a, b = input().split()
a = sorted(a)

for r in range(1, int(b) + 1):
    for i in combinations(a, r):
        print("".join(i))

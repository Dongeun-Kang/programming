from itertools import permutations

a, b = input().split()

p = sorted(permutations(a, int(b)))
for i in p:
    print("".join(i))

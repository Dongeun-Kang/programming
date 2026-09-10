n, s = map(int, input().split())

a = input().split()

liked = set(input().split())
disliked = set(input().split())

h = 0

for i in a:
    if i in liked:
        h += 1
    if i in disliked:
        h -= 1

print(h)

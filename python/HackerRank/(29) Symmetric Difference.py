s = set()

n1 = int(input())
m1 = set(map(int, input().split()))
n2 = int(input())
m2 = set(map(int, input().split()))


print("\n".join(map(str, sorted(m1 ^ m2))))

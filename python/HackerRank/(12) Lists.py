if __name__ == '__main__':
    N = int(input())
    results = []

    for i in range(N):
        s = input().split()
        match s[0]:
            case 'insert':
                i, e = list(map(int, s[1:]))
                results.insert(i, e)
            case 'print':
                print(results)
            case 'remove':
                e = int(s[1])
                results.remove(e)
            case 'append':
                e = int(s[1])
                results.append(e)
            case 'sort':
                results.sort()
            case 'pop':
                results.pop()
            case 'reverse':
                results.reverse()

def minion_game(string):
    lenOfString = len(string)
    kevin = 0
    stuart = 0
    for i in range(lenOfString):
        if string[i] in 'AEIOU':
            #kevin score
            kevin += lenOfString - i
        else:
            stuart += lenOfString - i
    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print(f"Stuart {stuart}")

if __name__ == '__main__':
    s = input()
    minion_game(s)

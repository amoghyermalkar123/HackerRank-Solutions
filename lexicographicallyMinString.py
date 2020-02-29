

def morganAndString(a, b):
    OUTPUT = []
    alphaIndex = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26

    }

    def comp(length, eq = False):
        TOP_i, TOP_j = 0, 0
        while TOP_j <= len(b) or TOP_i <= len(a):
            if TOP_j == len(b) or TOP_i == len(a):
                break
            else:
                if alphaIndex[a[TOP_i]] > alphaIndex[b[TOP_j]]:
                    OUTPUT.append(b[TOP_j])
                    TOP_j += 1

                elif alphaIndex[a[TOP_i]] < alphaIndex[b[TOP_j]]:
                    OUTPUT.append(a[TOP_i])
                    TOP_i += 1

                elif alphaIndex[a[TOP_i]] == alphaIndex[b[TOP_j]]:
                    OUTPUT.append(b[TOP_j])
                    TOP_j += 1

        if TOP_j == len(b):
            temp_split = []
            for temp in a[TOP_i:len(a)]:
                temp_split.append(temp)
            for remaining in temp_split:
                OUTPUT.append(remaining)

        elif TOP_i == len(a):
            tempo_split = []
            for tempo in b[TOP_j:len(b)]:
                tempo_split.append(tempo)
            for remn in tempo_split:
                OUTPUT.append(remn)


    if len(a) > len(b):
        comp(len(a))
    elif len(a) < len(b):
        comp(len(b))
    else:
        comp(len(a))
    return ''.join(OUTPUT)


a = morganAndString('AABABABABABABCCCCC', 'ABACABAABACABA')
print(a)

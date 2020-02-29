def countingValleys(n, s):
    sea_level = 0
    _Valleys = 0
    for i in range(n):
        if s[i] == 'U':
            sea_level += 1
            if sea_level == 0:
                _Valleys += 1
        elif s[i] == 'D':
            sea_level -= 1
        elif sea_level != 0 and i == n:
            print("wtf man")
        else:
            break
    print(_Valleys)


if __name__ == "__main__":
    countingValleys(8, "UDDDUDUU")

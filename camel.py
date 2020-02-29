def camelcase(s):
    count = 0
    for i in range(len(s)):
        if s[i].isupper():
            count += 1
    return count + 1


a = camelcase('saveChangesInTheEditorAmogh')
print(a)

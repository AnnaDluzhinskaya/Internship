def getIndex(s):
    s = s.replace(" ", "")
    s = s[6:len(s)].split("],")
    a = []
    for n in s[0].split(","):
        a.append(int(n))
    target = int(s[1][7:len(s[1])])
    for i in range(0,len(a)):
        if a[i] >= target:
            return i
    return len(a)

s = input()
print (getIndex(s))
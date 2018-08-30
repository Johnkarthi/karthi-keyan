ASCII = 256
def getMaxOccuringChar(s):
    count = [0] * ASCII
    x = -1
    c = ''
    for i in s:
        count[ord(i)]+=1;
    for i in s:
        if x < count[ord(i)]:
            x = count[ord(i)]
            c = i
    return c
s =input().split(' ')
print(" ".join(getMaxOccuringChar(k) for k in s))

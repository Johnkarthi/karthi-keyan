x = input("Enter file name: ")
b = 0
with open(x, 'r') as f:
    for c in f:
        if x.isdigit:
            b += 1
print(b)

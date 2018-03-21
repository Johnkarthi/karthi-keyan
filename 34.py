x = input("Enter file name: ")
y = 0
with open(x, 'r') as f:
    for c in f:
        y += 1
print(y)

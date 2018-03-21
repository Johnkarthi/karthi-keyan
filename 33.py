x = input("Enter file name: ")
y = 0
 with open(x, 'r') as f:
    for line in f:
        b = line.split()
        for i in b:
            for c in i:
                if(c.isspace):
                    y=y+1
print(y)

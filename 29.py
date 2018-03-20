t = input()
hour = t //60
t %= 60
minutes = t // 1
print("h:m-> %d:%d" % (hour,minutes))

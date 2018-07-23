def main():
    list=[]
    a,b=input().split(" ")
    a=int(a)
    b=int(b)
    for i in range(0,a):
        k=int(input())
        list.append(str(k))

    final=(list[-b:]+list[:-b])
    print( ' '.join(final))
if __name__ == '__main__':
    main()

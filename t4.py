def printMatrix(n, m):
    c=0
    for i in range(n):
        t=[]
        for i in range(m):
            c+=1
            t.append(c)
        print(*t)
        t=[]
n,m=map(int,input().split())
printMatrix(n,m)
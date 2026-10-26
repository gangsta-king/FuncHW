def isArmstrong(n=100,m=999):
    s=[i for i in range(n,m+1) if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i]
    print(*s)
isArmstrong()
    
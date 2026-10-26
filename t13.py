def printXPattern(n=int(input())):
    c=0
    for i in range(n//2,0,-1):
        print(' '*c+'*'+((i*2+1)-2)*' '+'*'+' '*c)
        c+=1
    print(' '*c+'*'+' '*c)
    c1=1
    for i in range(1,n//2+1):
        print(' '*c1+'*'+((i*2+1)-2)*' '+'*'+' '*c1)
        c1-=1
printXPattern()
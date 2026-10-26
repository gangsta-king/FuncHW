def printHollowSquare(n):
    print(n*'*')
    for i in range(n-2):
        print('*'+' '*(n-2)+"*")
    print(n*'*')
printHollowSquare(int(input()))
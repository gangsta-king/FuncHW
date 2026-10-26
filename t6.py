def isPrime(n=int(input()),m=int(input())):
    c=0
    for i in range(n,m+1):
        co=0
        for j in range(1,i+1):
            if i%j==0:
                co+=1
        if co==2:
            c+=1
    return 'Prime Count = ', c
print(*isPrime())
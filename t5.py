def isPrime(n=int(input())):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return 'Prime' if c==2 else 'noPrime'
print(isPrime())
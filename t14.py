def transformDigits(n=int(input())):
    s=''
    for i in str(n):
        if int(i)%2==0:
            s+=str(int(i)+1)
        else:
            s+=str(int(i)-1)
    print(int(s))
transformDigits()
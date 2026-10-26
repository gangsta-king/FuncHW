def binary(n):
    c=[]
    while n!=0:
        l=n
        c.append(str(l%2))
        n//=2
    return c
print(f'Binary = {int(''.join(binary(int(input()))[::-1]))}')
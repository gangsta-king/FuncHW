def isPalindrome(n=int(input())):
    v=n
    c=''
    while n!=0:
        c+=str(n%10)
        n//=10
    if int(c)==v:
        print('Palindrome')
    else:
        print('noPalindrome')
isPalindrome()
n = 29
flag = False
if n > 1:
    for i in range(2,n):
        if (n%i)==0:
            flag=True
            break
if flag:
    print(n,"it is not a prime")
else:
    print(n,"is  a prime")





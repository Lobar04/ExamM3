N = int(input('Son kiriting:'))
def tub_son(n):
    c = 0
    a = 1
    while n>c:
        for i in range(a,a+1):
            k = 0
            for j in range(1,i+1):
                if i%j==0:
                    k+=1
            if k!=2:
                yield i
                c+=1
        a+=1
print(list(tub_son(N)))

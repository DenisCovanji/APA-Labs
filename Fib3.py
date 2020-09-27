from datetime import datetime
start_time = datetime.now() 
def fib3(n):
    a=1
    b=0
    c=0
    d=1
    t=0
    count=13
    while n>0 :
        if n%2==1:
            t=b*d
            b=a*d+b*c+t
            a=a*c+t
            count+=6
        t=d**2
        d=2*c*d+t
        c=c**2+t
        n=n//2
        count+=7
    return b
g=fib3(int(input()))
print(g)
end_time = datetime.now()
print('Timpul: {}'.format(end_time - start_time))
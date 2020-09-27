#A recursive method
from datetime import datetime
start_time = datetime.now() 
def fib1(n):
    if n<2 :
        return n
    else:
        return fib1(n-1)+fib1(n-2)      
rez=fib1(int(input()))    
print(rez)
end_time = datetime.now()
print('Timpul: {}'.format(end_time - start_time))     
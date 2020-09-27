from datetime import datetime
start_time = datetime.now() 
def fib21(n):
    i,j=1,0
    k=1
    for k in range(n):
        j=i+j
        i=j-i
    return j    
res=fib21(int(input()))
print(res)
end_time = datetime.now()
print('Timpul: {}'.format(end_time - start_time))    


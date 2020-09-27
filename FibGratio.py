#Golden ratio
from datetime import datetime
start_time = datetime.now() 
fiblist = [0,1]
for i in range(int(input()) - 1):
    fiblist.append(fiblist[i] + fiblist[i+1])
print (fiblist)
gratio = [fiblist[i]/float(fiblist[i-1]) for i in range(2,len(fiblist))]
print (gratio)
end_time = datetime.now()
print('Timpul: {}'.format(end_time - start_time))
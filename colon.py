#basically we are trying to change the tuple ::::: so here we are trying to copy the tuple in such a way that
#the elements will be each copied differently using the deepcopy function and can be changed like a list 
#inside the tuple can be appended tc[4].append(50)
from copy import deepcopy
#create a tuple
t = ("Tutor", 'J', 23 , 56.67 , [23,12] , True) 
print(t)
#make a copy of a tuple using deepcopy() function
tc = deepcopy(t)
tc[4].append(50)
print(tc)
print(t)

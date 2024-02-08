t= (1,3,5,2,6,7,3,6,7,3,2,9,89,65,23,121)
def printRepeated(t):
    r=[]    
    for i in t:
        if(t.count(i)>1):
            if i not in r:
                r.append(i)
    print(list(r))

printRepeated(t)

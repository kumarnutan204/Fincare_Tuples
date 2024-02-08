t= (1,3,5,2,6,7,3,6,7,3,2,9,89,65,23,121)
#since tuple doesn't allow addition or removal of the items
# we can convert the tuple to a list and then perform removal
v= int(input("Enter the item to remove from the tuple"))

l=list(t)
for i in l:
    if (i==v):
        l.remove(i)
print(tuple(l))

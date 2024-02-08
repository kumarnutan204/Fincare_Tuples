tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# Use tuple slicing (tuple[start:stop]) 
# The start index is inclusive, and the stop index is exclusive.

# Slice from index 3 to 5 
_slice = tuplex[3:5]
print(_slice)
# If the start index isn't defined, it's taken from the beginning of the tuple by default
_slice = tuplex[:6]
print(_slice)

_slice = tuplex[5:]
print(_slice)
# If neither start nor end index is defined, it returns the full tuple.
_slice = tuplex[:]
print(_slice)

# Slice from -8 to -4 
_slice = tuplex[-8:-4]
print(_slice)

tuplex = tuple("GOOD PROGRAM")
print(tuplex)

# tuple[start:stop:step]

# Slice from index 2 to 9 with a step of 2 
_slice = tuplex[2:9:2]
print(_slice)

# Slice with a step of 4, which returns a tuple with a jump every 3 items
_slice = tuplex[::4]
print(_slice)

# When the step is negative, it reverses the order, slicing from index 9 to 2 with a step of -4
_slice = tuplex[9:2:-4]
print(_slice)
#reverse print the tuple 
print(tuplex[::-1])

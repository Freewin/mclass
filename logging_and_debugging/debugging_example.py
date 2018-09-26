import pdb

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in values:
    mysum = 0       # intential mistake to find in the debugger
    mysum = mysum + val
    pdb.set_trace()


print(mysum)

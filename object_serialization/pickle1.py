import pickle


my_list = ['a', 'b', 'c', 'd', 'e']

with open('myfile.txt', 'wb') as fh:
    pickle.dump(my_list, fh)

with open('myfile.txt', 'rb') as fh:
    unpickedlist = pickle.load(fh)


print(unpickedlist)

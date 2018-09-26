import pickle

x = pickle.dumps(['a', 'b', 1, 2.3])

var = pickle.loads(x)

print(var)
print(type(x))
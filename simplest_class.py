

class MyClass(object):
    pass

class MyOtherClass(object):
    myvar = 10

this_obj = MyClass()
print(this_obj)

that_obj = MyClass()
print(that_obj)

print()
print()

obj1 = MyOtherClass()
obj2 = MyOtherClass()

print(obj1.myvar)
print(obj2.myvar)

print()
print()
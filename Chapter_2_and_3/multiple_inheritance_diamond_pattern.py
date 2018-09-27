# Example of diamond shape inheritance pattern presented in class


class A(object):

    def dothis(self):
        print("Doing this in A")


class B(A):
    pass


class C(A):

    def dothis(self):
        print("Doing this from C")


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()

# Method Resolution Order
print(D.mro())

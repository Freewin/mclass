class Joe(object):
    gretting = "Hello World"

    def callme(self):
        print("calling \"callme\" method with instance: ", self)

thisJoe = Joe()
print (thisJoe.gretting)

thisJoe.callme()

print()
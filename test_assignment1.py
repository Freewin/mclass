from assignments.assignment1 import MaxSizeList

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("Hey")
a.push("Hi")
a.push("Let's")
a.push("go")

b.push("Hey")
b.push("Hi")
b.push("Let's")
b.push("go")

print(a.get_list())
print(b.get_list())
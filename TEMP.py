
class Parent:
    val = 10
    def __init__(self, val):
        self.val = val

    def foo(self):
        self.val = self.val + 4

class Child(Parent):
    val2 = 0
    def __init__(self, val):
        self.val = val
        self.val2 = val * 2.0

    def funk(self):
        self.val = self.val - 1
        self.val2 = self.val2 * 4.0

Obj0 = Child(3)
Obj1 = Child(5)
Obj2 = Parent(4)

print("Obj0:" + str(Obj0.val) + " " + str(Obj0.val2))
print("Obj1:" + str(Obj1.val) + " " + str(Obj1.val2))

Obj0.foo()
Obj0.funk()
Obj2.foo()

print("Obj0:" + str(Obj0.val) + " " + str(Obj0.val2))
print("Obj1:" + str(Obj1.val) + " " + str(Obj1.val2))

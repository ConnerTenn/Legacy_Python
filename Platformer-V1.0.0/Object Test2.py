
class Program():
    def Main(self):
        Object1 = ObjectClass(1,2,3,4,5,6)
        Object2 = ObjectClass(7,8,9,10,11,12)
        Object3 = ObjectClass(13,14,15,16,17,18)

        print(Object1.Value1)
        Object1.Func1()

        print()
        
        print(Object2.Value1)
        Object2.Func1()

        print()
        print()
        print('Done')

class ObjectClass():
    def __init__(self, in1, in2, in3, in4, in5, in6):
        self.Value1 = in1
        self.Value2 = in2
        self.Value3 = in3
        self.Value4 = in4
        self.Value5 = in5
        self.Value6 = in6
        
    def Func1(self):
        print(self.Value5)


Program =Program()
Program.Main()

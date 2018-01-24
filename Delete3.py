class Main_Class:
    def Main():
        Num=Main_Class.Get_Num(5)
        print("Ans:%s" % (Num))
         
    def Get_Num(Value):
        return Value * 5
        
Main_Class=Main_Class
Main_Class.Main()

class a():
    def printf(self):
        print("ha")

def b():
    
    for x in range(1,6):
        aa="global var%s; var%s = a()" % (str(x), str(x))
        print(aa)
        exec(aa)
        list1.append("print(var%s)" % (x))

list1 = []
b()

print()
for item in list1:
    exec(item)

print('done')

        

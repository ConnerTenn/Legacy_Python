class a():
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def Recall(self):
        print('X:%s, Y%s' %(self.x,self.y))
    def Move_Up(self):
        self.y=self.y+1
    def Move_Down(self):
        self.y=self.y-1
    def Move_Left(self):
        self.x=self.x-1
    def Move_Right(self):
        self.x=self.x+1
s=a(3,3)
s.Recall()
print()
Play=True
while Play==True:
    Direction=(str(input("Direction: ")))
    Direction=Direction.upper()
    print(Direction)
    if Direction=='W':
        s.Move_Up()
    elif Direction=='S':
        s.Move_Down()
    elif Direction=='A':
        s.Move_Left()
    elif Direction=='D':
        s.Move_Right()
    elif Direction=='Q':
        Play=False
    s.Recall()

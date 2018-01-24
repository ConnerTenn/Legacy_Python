print "-------"
print "|@    |"
print "-------"
a = str(raw_input("a="))
x = 1
while a != "q":
    for w in range(15):
        print ""
    if x >= 5:
        direction = 1
    if x <= 1:
        direction = 2
    if direction == 1:
        x = x - 1
    if direction == 2:
        x = x + 1
    from time import sleep
    sleep(0.5)
    if x == 1:
        print "-------"
        print "|@    |"
        print "-------"
    if x == 2:
        print "-------"
        print "| @   |"
        print "-------"
    if x == 3:
        print "-------"
        print "|  @  |"
        print "-------"
    if x == 4:
        print "-------"
        print "|   @ |"
        print "-------"
    if x == 5:
        print "-------"
        print "|    @|"
        print "-------"
print "END"

        


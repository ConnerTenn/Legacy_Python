print "-------"
print "|@    |"
print "-------"
a = str(raw_input("a="))
x = 1
while a != "q":
    for w in range(15):
        print ""
    if a == "d":
        if x < 5:
            x = x + 1
    if a == "a":
        if x > 1:
            x = x - 1
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
    a = str(raw_input("a="))
print "END"

        

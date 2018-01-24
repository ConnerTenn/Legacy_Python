import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def tile1():
    cls()
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@@          "
    print "@@@@          "
    print "@@@@          "
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile1()
    elif a == "s":
        tile4()
    elif a == "a":
        tile1()
    elif a == "d":
        tile2()
    else:
        tile1()

def tile2():
    cls()
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "              "
    print "              "
    print "              "
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile2()
    elif a == "s":
        tile5()
    elif a == "a":
        tile1()
    elif a == "d":
        tile3()
    else:
        tile2()

def tile3():
    cls()
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "          @@@@"
    print "          @@@@"
    print "          @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile3()
    elif a == "s":
        tile6()
    elif a == "a":
        tile2()
    elif a == "d":
        tile3()
    else:
        tile3()

def tile4():
    cls()
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@          "
    print "@@@@          "
    print "@@@@          "
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile1()
    elif a == "s":
        tile7()
    elif a == "a":
        tile4()
    elif a == "d":
        tile5()
    else:
        tile4()

def tile5():
    cls()
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "          @@@@"
    print "          @@@@"
    print "          @@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@-FINISH-@@@"
    print "@@@@@@@@@@@@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT    q = QUIT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile2()
    elif a == "s":
        tile5()
    elif a == "a":
        tile4()
    elif a == "d":
        tile5()
    elif a == "q":
        end()
    else:
        tile5()

def tile6():
    cls()
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile3()
    elif a == "s":
        start()
    elif a == "a":
        tile6()
    elif a == "d":
        tile6()
    else:
        tile5()

def tile7():
    cls()
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@          "
    print "@@@@          "
    print "@@@@          "
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile4()
    elif a == "s":
        tile7()
    elif a == "a":
        tile7()
    elif a == "d":
        tile8()
    else:
        tile7()

def tile8():
    cls()
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "              "
    print "              "
    print "              "
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@@@@@@@@@@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile8()
    elif a == "s":
        tile8()
    elif a == "a":
        tile7()
    elif a == "d":
        start()
    else:
        tile8()
    
def start():
    cls()
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "@@@@      @@@@"
    print "          @@@@"
    print "          @@@@"
    print "          @@@@"
    print "@@@@@@@@@@@@@@"
    print "@@@-START-@@@@"
    print "@@@@@@@@@@@@@@"
    print""
    print" w = UP    s = DOWN    a = RIGHT    d = LEFT"
    a = str(raw_input("Direction="))
    if a == "w":
        tile6()
    elif a == "s":
        start()
    elif a == "a":
        tile8()
    elif a == "d":
        start()
    else:
        start()

def end():
    print "GOOD BYE"

start()


    

#======================
#|   All Subs Must    |
#|  Be Written At The |
#|      Beginning     |
#======================

def choice1():
    print "You Typed 1"
def choice2():
    print "You Typed 2"
def start():
    a = int(raw_input("a="))
    if a == 1:
        choice1()
    elif a == 2:
        choice2()
    else:
            print "Try Again"
    start()

# End Of Subs

start()






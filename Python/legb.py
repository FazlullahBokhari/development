#LEGB Rule ---> Local Enclosing Global Built in

def report():
    # local Assignment!!
    x = "local"
    print(x)
report()

x = "This is global level"

def enclosing():
    x = "Enclosing level"

    def inside():
        print(x)
    inside()
enclosing()

def globalfun():
    def inside1():
        print(x)
    inside1()
globalfun()

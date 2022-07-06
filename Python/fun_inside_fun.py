def hello():
    return "Hi Faiz"

def other(func):
    print("Some other code")
    # assume that func passed in is a function!!
    print(func())
other(hello)

def hello(name="Faiz"):
    print("The hello() function has been run")
    def greet():
        return "       This is inside the greet()"
    def welcome():
        return "       This is inside welcome"
    print(greet())
    print(welcome())
    print("-------------------")
    if name == "Faiz":
        return greet
    else:
        return welcome

x = hello(name="Fazlullah")
print(x())

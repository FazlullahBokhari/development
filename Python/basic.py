x = "outside"

def report():
    x = "inside"
    return x

print(report())
print(x)

y = "This is global level Y"

def fun():
    global y
    y ="This is local level Fun"
    return y
print(fun())
print(y)

z = "Global level Z"
def fun1(z):
    z = "local level Fun1"
    return z
print(fun1(z))
print(z)

#LEGB Rule ---> Local Enclosing Global Built in

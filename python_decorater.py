def fun_dec1(fun):
    print("Decorator is called")
    return fun


def fun_dec2(fun):    
    print("Decorator is called")
    def inner(*args, **kwargs):
        print("Inner function is called")
        return fun(*args, **kwargs)
    return inner

@fun_dec1
def add(a, b):
    print("Add function is called")
    return a + b


add(10, 20)
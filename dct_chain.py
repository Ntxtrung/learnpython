def function1(func):
    def inner():
        x = func()
        return x*x
    return inner

def function(func):
    def inner():
        x = func()
        return  x*2
    return inner

@function
@function1

def num():
    return  10

print(num())
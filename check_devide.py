def smart_divide(func):
    def inner(a,b):
        print(f"I am going to divide{a} and {b}")
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)

divide(1,2)
divide(1,0)    
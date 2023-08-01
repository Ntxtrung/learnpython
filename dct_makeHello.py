def make_hello(func):
    def inner():
        print("Hello all,", sep="")
        func()
    return inner

@make_hello
def welcome():
    print("Welcome to Vinamation")

welcome()
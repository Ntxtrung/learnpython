def power(n):
    return lambda a : a ** n

base = power(2)
print(f"8 power of 2 = {base(8)}")
base = power(8)
print(f"8 power of 8 = {base(8)}")
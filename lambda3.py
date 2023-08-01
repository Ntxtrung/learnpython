numbers = [1,4,5,7,8,12,16]

new_numbers = list(filter(lambda x: (x%2 == 0), numbers))
print(new_numbers)
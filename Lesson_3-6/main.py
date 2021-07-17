
# import sys
# a = sys.argv

# import module_1

# print(f"Hello, I am a module {__name__}")
# # print(f"Hello, I am a module {module_1.__name__}")
# print(f"module 1: {module_1.vaiable_1}")

from calculations import prime_numbers

input_list = [1,2,3,4,5,6,7,8,9,10]

prime_numbers = prime_numbers.get_prime_numbers_count(input_list)

print(prime_numbers)

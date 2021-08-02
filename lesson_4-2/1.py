import sys


# my_list = [i for i in range (50_000_000)]
#
# my_iter = iter(my_list)
#
# print(len(my_list))
# print(sys.getsizeof(my_list))

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# ii = iter(ll)

# while True:
#     try:
#         print(next(ii))
#     except StopIteration:
#         break

def generator(n):
    i = 0
    while i < n:
        i += 1
        yield i


for i in generator(10):
    print(i)

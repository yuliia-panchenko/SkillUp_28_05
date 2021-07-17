"""Module descriptions"""


def get_prime_numbers_count(source_list):
    """Return the list of prime numbers"""
    result = []
    for number in source_list:
        if number % 2 == 0:
            result.append(number)

    return result

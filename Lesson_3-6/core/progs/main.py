from core.modules.module_a import get_prime_numbers_count


def run_program():
	input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	prime_numbers = get_prime_numbers_count(input_list)

	print(prime_numbers)

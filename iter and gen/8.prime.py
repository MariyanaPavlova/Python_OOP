def get_primes(numbers):

    for num in numbers:
        if is_prime(num):
            yield num

def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
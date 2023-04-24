def is_palindrome(n):
    if isinstance(n, int):
        return str(n) == str(n)[-1::-1]
    else:
        raise TypeError(f'Error: n = {n} must be int!')
    

def is_prime(n):
    if isinstance(n, int):
        return sum([n % div == 0 for div in range(1, n + 1)]) == 2
    else:
        raise TypeError(f'Error: n = {n} must be int!')

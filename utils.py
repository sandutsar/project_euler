def is_palindrome(n):
    if isinstance(n, int):
        return str(n) == str(n)[-1::-1]
    else:
        raise TypeError(f'Error: n = {n} must be int!')

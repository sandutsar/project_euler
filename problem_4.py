import sys
from utils import is_palindrome


def problem_4(limit=3):
    result = []
    for x in range(10**(limit-1), 10**limit):
        for y in range(10**(limit-1), 10**limit):
            if is_palindrome(x*y):
                result += [x*y]
    return max(result)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(problem_4(*map(int, sys.argv[1:])))
    else:
        print(problem_4())

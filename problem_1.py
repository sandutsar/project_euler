import sys


def problem_1(a=3, b=5, limit=int(1e3)):
    result = sum([num if num % a == 0 or num % b == 0 \
                  else 0 for num in range(limit)])
    return result


if __name__ == '__main__':
    if len(sys.argv) in [3, 4]:
        print(problem_1(*map(int, sys.argv[1:])))
    else:
        print(problem_1())

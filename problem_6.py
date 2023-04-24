import sys


def problem_6(limit=100):
    return sum([x for x in range(limit + 1)])**2 - \
        sum([x*x for x in range(limit + 1)])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        limit = int(sys.argv[1])
        print(problem_6(limit=limit))
    else:
        print(problem_6())

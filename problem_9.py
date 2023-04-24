import sys


def problem_9(limit=1000):
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                if a + b + c == limit and a*a + b*b == c*c:
                    return a*b*c


if __name__ == '__main__':
    if len(sys.argv) == 2:
        limit = int(sys.argv[1])
        print(problem_9(limit=limit))
    else:
        print(problem_9())

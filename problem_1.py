def problem_1(a=3, b=5, limit=int(1e3)):
    result = []
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            result += [num]
    return sum(result)


if __name__ == '__main__':
    print(problem_1())

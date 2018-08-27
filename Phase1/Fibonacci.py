def main():
    print(fib(5))


def fib(num):
    fibo = [0, 1]
    for i in range(num):
            fibo.append(fibo[-2] + fibo[-1])
    return fibo


if __name__ == '__main__':
    main()

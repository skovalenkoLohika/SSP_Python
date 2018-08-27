def main():
    try:
        n = int(input("Enter number of terms:"))
        print(fib(n))
    except ValueError:
        print('you have inputted wrong number')



def fib(num):
    fibo = [0, 1]
    if type(num) == int:
        if num >=2:
            for i in range(num):
                fibo.append(fibo[-2] + fibo[-1])
            return fibo
        else:
            print('please input more than 1')
    else:
        print('You can input only digits')

if __name__ == '__main__':
    main()

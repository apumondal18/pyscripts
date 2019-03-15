n = int(input("Input a number: "))

def fib(k):
    if k == 1 or k == 2:
        return 1
    else:
        return fib(k-1) + fib(k-2)

cal_fib = fib(n)
print("Fibonacci nunber for ",n,"is",cal_fib)
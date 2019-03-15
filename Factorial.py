n = int(input("Input number here to get the factorial: "))

def fact(k):
    if k == 1:
        return 1
    else:
        return k * fact(k-1)

f = fact(n)

print(f"Factorial for the number {n} is", f)
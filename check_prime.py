k = n = int(input("Input number here to check if prime: "))


for i in range(2,n):
    if k == 2:
        print("Number is prime")
    if k % i != 0:
        if k-1 == i:
            print(f"{n} is prime")
    else:
        print(f"{n} NOT Prime")
        break

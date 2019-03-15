#n= int(input("Give Pyramid Height: "))
n=4
for i in range(n+1):
    print('*'* i)

print(25*'-')

l=1
for i in range(n,0, -1):
    print(i * ' '+ l * '*')
    l += 1

print(25*'-')

m=1
for i in range(n,0, -1):
    print(i * ' '+ m * '* ')
    m += 1

print(25*'-')

k=1
for i in range(n,0, -1):
    print(i * ' '+ k * '*')
    k += 2

print(25*'-')


for i in range(n,0,-1):
    print(i * '*')

print(25*'-')

l=0
for i in range(n,0,-1):
    print(l*' '+i*'*')
    l += 1
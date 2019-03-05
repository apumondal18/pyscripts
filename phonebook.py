n=int(input())
dict01={}
for i in range(1,n+1):
    sp=input()
    sp.split()
    dict01[sp.split()[0]] = sp.split()[1]

a=1
while a == 1:
    name=input()
    if name in dict01:
        print(name,"=",dict01[name])
    else:
        print('Not found')

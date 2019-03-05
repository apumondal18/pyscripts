n = int(input())
m = 0
max1 = 0
bn = bin(n)
bin_num = bn.split('b')[1]
for i in bin_num:
    if i == '1':
        m = m + 1
        if max1 < m:
            max1 = m

    else:
        m = 0
print(max1)
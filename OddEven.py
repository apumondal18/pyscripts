n = int(input())
for i in range(0,n):
    inp_str = input()
    str_len = len(inp_str)
    even_str = ''
    odd_str = ''
    for i in range(0,str_len,2):
        even_str = even_str + inp_str[i]
    for i in range(1,str_len,2):
        odd_str = odd_str + inp_str[i]
    print(even_str,odd_str)
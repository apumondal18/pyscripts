from sys import argv
#run with 2 parameters, 1st parameter will be the scriptname
a,b,c = argv

print(a)
print(b)
print(c)

txt = open(a)
print(f"I'm going to print out the file content of {a}")
print(txt.read())
txt.close()
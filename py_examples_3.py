def names(*babies):
    a, b = babies
    print(f"Babies are {a} and {b}")

def diff_babies(baby1, baby2):
    print(f"Babies are {baby1} and {baby2}")

def cute_baby(baby):
    print(f"My {baby} is cute")

def nobaby():
    print("I don't have a baby")

#lets call the babies
names('Ana','Rock')
diff_babies('Shyam','Prem')
cute_baby('Adrija')
nobaby()

def printline(filename):
    print(filename.readline())

cfile = open("py_examples_3.py")

printline(cfile)
printline(cfile)
print(cfile.read())
cfile.close()

def addition(a,b):
    return a+b

print(addition(2,5))

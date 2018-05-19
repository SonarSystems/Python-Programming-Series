varGlobal = 1

def AwesomeFunction():
    "This function is awesome"
    print("Hello World")
    print("My name is bob and no i cannot fix it")
    return

AwesomeFunction()
AwesomeFunction()
AwesomeFunction()

def AwesomeFunction2(number1, number2):
    "Adds the numbers together"
    return number1 + number2
    
print(AwesomeFunction2(5, 6))

var1 = 5
print(var1)

def ChangeFunction(number1):
    "Change function"
    number1 = 8
    return

print(var1)


def DefaultArg(var1 = 8):
    return var1 * 2
    
print(DefaultArg(9))
print(DefaultArg())
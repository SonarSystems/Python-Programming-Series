#Assert statement
def Function1(var1):
    assert(var1 != 0), "Zero is invalid"
    return 10 / var1

print(Function1(4))

try:
    file = open("Text.txt", "w")
    file.write("Hello")
except IOError:
    print("File not found")
else:
    print("A OK")
    file.close()

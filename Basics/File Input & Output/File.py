import os

print("Hello World")

#var1 = input("Enter something please: ")
#print(var1)

var2 = open("File.txt", "r+")
print(var2)
print(var2.name)



#var2.write("Hello My Name Is Bob")

string1 = var2.read(10)

print(string1)


var2.close()

#os.rename("File.txt", "New Name.txt")
#os.remove("Filelocation and filename")

os.mkdir("New Folder")

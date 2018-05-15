var1 = "Hello World"

for character in var1:
    if character == ' ':
        print("There was a space, oh no")
        break
    print(character)
    
    
for character in var1:
    if character == ' ':
        print("There was a space, lets skip this iteration")
        continue
    print(character)
    
for character in var1:
    if character == ' ':
        pass
        print("Passing this over")
    print(character)
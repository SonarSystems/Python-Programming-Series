listNumber1 = [1, 2, 3, "Hello", "World", 4, 5, 6]

# Access
print(listNumber1)
print(listNumber1[2])

# Update
print(listNumber1[0])
listNumber1[0] = "Bob"
print(listNumber1[0])

# Delete
print(listNumber1)
del listNumber1[1]
print(listNumber1)

print(len(listNumber1))
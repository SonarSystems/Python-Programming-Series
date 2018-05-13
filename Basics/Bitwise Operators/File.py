var1 = 13   #   1101
var2 = 5    #   0101

# 13    1101
# 5     0101
#       ----
# AND   0101 (5)
print (var1 & var2)

# 13    1101
# 5     0101
#       ----
# OR    1101 (13)
print (var1 | var2)


# 13    1101
# 5     0101
#       ----
# XOR   1000 (8)
print (var1 ^ var2)

# 13                    1101
# Ones Complement       
print (~var1)

# Binary Shift Left
print (var1 << 1)

# Binary Shift Right
print (var1 >> 1)
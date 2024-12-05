str1 = "23"
int1 = 14

print(str1, "is a ", type(str1))
print(int1, "is an ", type(int1))

print("After type casting")
str2 = str(int1) 
print(str2, " is a", str2)



str2 = int(str)
print(str2, " is a ", type(str2))
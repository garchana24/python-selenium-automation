name = input("Enter a name:")
split_name = name.split()
print(split_name)
x1 = split_name[0]
print(x1)
x2 = split_name[1]
print(x2)
initials = x1[0:1].upper() +"."+x2[0:1].upper()
print(initials)



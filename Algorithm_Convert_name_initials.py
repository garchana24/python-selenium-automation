name = input("Enter a name:")
split_name = name.split()
#print(split_name)
x1 = split_name[0].split()
nlist1 = list(x1[0])
x2 = split_name[1].split()
nlist2 = list(x2[0])

print(name + "=>" + nlist1[0].upper() + "." + nlist2[0].upper())


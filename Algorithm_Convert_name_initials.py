name = input("Enter a name:")
split_name = name.split()
print(len(split_name))
length = (len(split_name))
#for i in range(length):
#    if(i > 1):
#        print("Please enter name with only 2 words")
assert length == 2, f'Error! Please enter only two word names'

x1 = split_name[0]
print(x1)
x2 = split_name[1]
print(x2)
initials = x1[0:1].upper() +"."+x2[0:1].upper()
print(initials)

"""phrase = 'amazon'
set_phrase = set('amazon')
string = ''.join([str(item) for item in set_phrase])
print((string))"""





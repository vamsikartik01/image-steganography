## this char.py file has the operations we need for converting the character into binary

string = "This image is a black hole"
char = "B"

# to get each character from the string we can simply say.
for _ in string:
    print(_,end="|")

# finding the ASCII value is very simple in python
val = ord(char)
print("\nThe ASCII value of the B is",val)

# convert the ascii value into binary...
bin_val = format(val, "08b")
print(bin_val) #bin_val is a string





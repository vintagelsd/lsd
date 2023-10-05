input_str = input()
a = ""
b = ""
zxc = False
for char in input_str:
    if char != ' ' and char != ',':
        if not zxc:
            a += char
        else:
            b += char
    elif char == ',':
        zxc = True
a = float(a)
b = float(b)
с = a % b
print(с)
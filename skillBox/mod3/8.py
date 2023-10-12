pnumber = input()
cnumber = ''.join(char for char in pnumber if char.isdigit() or char == '+')
print(cnumber)
zxc = input()
space1 = zxc.find(' ')
space2 = zxc.rfind(' ')
a = int(zxc[:space1])
b = int(zxc[space1+1:space2])
c = int(zxc[space2+1:])
min_num = min(a, b, c)
max_num = max(a, b, c)
if a != min_num and a != max_num:
    mid_num = a
elif b != min_num and b != max_num:
    mid_num = b
else:
    mid_num = c
print(mid_num)

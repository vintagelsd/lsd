a = input()
last_dot = len(a)
for i in range(len(a)-1, -1, -1):
    if a[i] == '.':
        print(a[i+1:last_dot])
        last_dot = i
print(a[0:last_dot])
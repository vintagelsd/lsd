input_str = input()
i = input_str[-1]
count = 0
for char in input_str:
    if char == i:
        count += 1
    else:
        break
print(count)

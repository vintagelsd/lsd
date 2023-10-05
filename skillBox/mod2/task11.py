def has_duplicates(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False
input_str = input()
numbers_str = ""
numbers = []
for char in input_str:
    if char.isdigit() or char == '-' or char == ' ':
        numbers_str += char
    elif numbers_str:
        numbers.append(int(numbers_str))
        numbers_str = ""
if numbers_str:
    numbers.append(int(numbers_str))
result = has_duplicates(numbers)
print(result)
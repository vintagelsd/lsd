input_str = input()
words = []
current_word = ""
for char in input_str:
    if char != ' ':
        current_word += char
    else:
        words.append(current_word)
        current_word = ""
if current_word:
    words.append(current_word)
new_word = ""
for word in words:
    new_word += word[-1]
print(new_word)

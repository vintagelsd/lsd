def clean_phone_number(phone_number):
    cleaned_number = ''.join(char for char in phone_number if char.isdigit() or char == '+')
    return cleaned_number
phone_number = input()
cleaned_number = clean_phone_number(phone_number)
print(cleaned_number)

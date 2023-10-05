def count_vowels_and_consonants(s):
    a = "аеёиоуыэюяaeiouy"
    b = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        char = char.lower()

        if char in a:
            vowel_count += 1
        elif char in b:
            consonant_count += 1

    return vowel_count, consonant_count
s = input()
a, b = count_vowels_and_consonants(s)
print(a, b)
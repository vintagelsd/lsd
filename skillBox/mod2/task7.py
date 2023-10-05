def check_zeros_and_ones(s):
    zeros = s.count('0')
    ones = s.count('1')

    if zeros == ones:
        return 'yes'
    else:
        return 'no'
s = input()
result = check_zeros_and_ones(s)
print(result)

n = float(input())
z = ''
x = ''
c = ''
hex_digits = "0123456789ABCDEF"
if n != int(n):
    print("Анлаки еще разок трайни")
else:
    n = int(n)
    n1 = int(n)
    n2 = int(n)
    if n <= 0:
        print("Анлаки еще разок трайни")
    else:
        while n > 0:
            b = str(n % 2) + z
            n = n // 2
        while n1 > 0:
            o = str(n1 % 8) + x
            n1 = n1 // 8
        while n2 > 0:
            h = hex_digits[n2 % 16] + c
            n2 = n2 // 16
print(z, x, c)


a = int(input())
b = int(input())
c = int(input())
if a == b and a == c and b == c:
    print('Все числа равны')
elif a != b and a != c and b != c:
    print('Все числа разные')
else:
    print('Есть равные и неравные числа')

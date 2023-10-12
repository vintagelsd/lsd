n = input()
print(f"{int(n):b}, {int(n):o}, {int(n):X}" if n.isnumeric() and int(n) > 0 else "Неверный ввод")

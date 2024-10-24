def find_password(n):
    pairs = []
    for i in range(1, n//2 + 1):
        pairs.append((i, n - i))
    password = ''.join(str(x) + str(y) for x, y in pairs)
    return password

n = int(input("Введите число от 3 до 20: "))
result = find_password(n)
print(f"Нужный пароль: {result}")


# Первый пример для отладки
transactions = [100, 200, 90, 70, 120]
# Второй пример для отладки
# transactions = [100, 98, 1000, 2500, 299, 1898, 1989, 2001, 50, 10, 70]


n = len(transactions)
for i in range(n - 2):
    for j in range(n - 2 - i):
        if transactions[j] > transactions[j + 1]:
            transactions[j], transactions[j + 1] = transactions[j + 1], transactions[j]

if transactions[-2] > transactions[-1]:
    transactions[-2], transactions[-1] = transactions[-1], transactions[-2]
print(transactions)
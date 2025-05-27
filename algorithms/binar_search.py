
numbers_list = [0, 20, 30, 34, 45, 56, 67, 78, 90, 100, 110]
key = 89

# Первый пример для отладки
# numbers_list = [100, 200, 700, 1000, 1200]
# key = 1000

left = 0
right = len(numbers_list) - 1
flag = False
counter = 0

while left <= right:
    center = (left + right) // 2
    counter += 1
    if key == numbers_list[center]:
        flag = True
        break
    if key < numbers_list[center]:
        right = center - 1
    else:
        left = center + 1

print(f"{flag}, {counter}")
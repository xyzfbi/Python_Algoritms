numbers_list = [1, 3, 7, 1, 1, 2, 3, 7, 6, 5, 5, 4, 1, 5, 9, 1, 7, 0, 0]

# Способ 1.
result = 0
'''for i in range(len(numbers_list)):
    flag = False
    for j in range(len(numbers_list)):
        if i != j and numbers_list[i] == numbers_list[j]:
            flag = True
            break
    if not flag:
        result = numbers_list[i]
print(result)'''

# Способ 2
'''freq_list ={}
for number in numbers_list:
    if number in freq_list:
        freq_list[number] += 1
    else:
        freq_list[number] = 1
for number in freq_list:
    if freq_list[number] == 1:
        print(number)'''

# Способ 3
result = 0
for number in numbers_list:
    result ^= number # ВСЕ ПАРЫ ЧИСЕЛ ЗАНУЛЯЮТСЯ А ОСТАЕТСЯ В ИТОГЕ УНИКАЛЬНОЕ
    # ЗАДАЧКА ЖЕСТКАЯ
print(result)

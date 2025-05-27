
file1 = [1, 5, 6, 18, 42, 74, 80, 87, 91, 99, 100]
file2 = [2, 3, 5, 7, 8, 18, 19, 20, 43, 50, 81, 93, 101]

result = []

i, j = 0, 0
while i < len(file1) and j < len(file2):
    if i < len(file1) and j < len(file2):
        if file1[i] < file2[j]:
            result.append(file1[i])
            i += 1
        else:
            result.append(file2[j])
            j += 1
    elif i < len(file1):
        result.append(file1[i])
        i += 1
    else:
        result.append(file2[j])
        j += 1
print(result)

numbers_list = [2, 12, 7, 8, 0]

result = []
window_size = 2


for i in range(len(numbers_list) - window_size + 1):


    temp = sum(numbers_list[i:i + window_size]) / window_size # average window
    result.append(temp)
    
print(result)
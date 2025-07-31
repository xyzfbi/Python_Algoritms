from itertools import combinations, permutations, product

print(list(combinations('ABC', 2)))  # [('A','B'), ('A','C'), ('B','C')]
print(list(permutations('ABC', 2)))
print(list(product('ABC', 'GD')))
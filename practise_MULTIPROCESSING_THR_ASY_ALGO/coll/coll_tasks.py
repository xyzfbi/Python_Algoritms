import collections


def task_1():
    transactions = [100, 50, 200, 150, 50, 200, 200]
    c = collections.Counter(transactions)
    sum_c = sum(transactions)
    common = c.most_common(1)[0][0]
    len_unique = len(c)
    print(c, sum_c, common, len_unique)


def sliding_average(values, n):
    window = collections.deque(maxlen=n)
    average = []
    for value in values:
        window.append(value)
        if len(window) == n:
            average.append(sum(window) / len(window))

    return average


def task_3(lst):
    n_unique = collections.defaultdict(set)
    for item in lst:
        first_ltr = item[0]
        n_unique[first_ltr].add(item)
    n_unique = ({k: list(v) for k, v in n_unique.items()})
    return n_unique

def task_4():
    Book = collections.namedtuple('Book', 'title author year')
    books = [
        Book("pashalka", "Z", "1999"),
        Book("goyda", "WW", "2007"),
        Book("kumar", "O", "2014"),
    ]
    return min(books, key=lambda book: book.year)
def task_5():
    default = {'color': 'red', 'size': 'M'}
    user = {'color': 'blue', 'theme': 'dark'}
    chain = collections.ChainMap(user, default)
    return chain
'''
trans_usa = [1, 3, 5, 7, 9, 2, 4, 6, 8]
result = sliding_average(trans_usa, 3)
print(result)

print(task_3(["apple", "banana", "apple", "cherry", "banana", "apple"]))
print(task_4())'''
ch = task_5()
print(ch['color'])
print(ch['size'])
print(ch['theme'])
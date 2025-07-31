from itertools import product, combinations, groupby, count, islice, chain


def task_1():
    colors = ['Red', 'Blue', 'Green', 'Yellow']
    sizes = ['Small', 'Medium', 'Large']
    materials = ['Cotton', 'Polyester']

    print(list(product(colors, sizes, materials)))


def task_2():
    lst = [1, 2, 3]
    print(list(combinations(lst, 2)))


def task_3():
    suits = ['♠', '♥', '♦', '♣']
    ranks = [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'A']

    deck = [rank + suit for suit in suits for rank in ranks]
    print(deck)
    same_deck = [c for c in combinations(deck, 2) if c[0][1] == c[1][1]]
    print(same_deck)
    ranks_same_deck = [c for c in combinations(deck, 2) if c[0][0] == c[1][0]]
    print(ranks_same_deck)



def task_4():
    def grouper(value):
        if value < 18.5: return "Cool"
        elif 18.5<= value <= 19.5: return "Mild"
        else: return "Hot"

    temperatures =  [18.2, 18.0, 17.8, 19.1, 20.5, 19.9, 18.7]
    temperatures = sorted(temperatures, key=grouper)
    grouped = groupby(temperatures, key=grouper)

    for key, value in grouped:
        print(f"{key}: {list(value)}")


def task_5():
    squares = (x ** 2 for x in count(1))
    first_10 = list(islice(squares, 10))
    print(first_10)


def task_6():
    squares = (x * x for x in range(3))  # 0,1,4
    cubes = (x ** 3 for x in range(2))  # 0,1
    primes = [2, 3, 5]

    combined = chain(squares,primes, cubes)
    print(list(combined))


task_6()

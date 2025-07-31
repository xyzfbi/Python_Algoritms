import collections

str = "asdfghzxcvbm,ml;slldiaufyhdsfgeyuhwjscgdfukgahwjdgkagdafsdcfafdgawyfgrdkjjkskldhgflhkrjityedhcxjksjlasfghalkdfsjfgksf;glkdfjuthdistofkdndjxzklcvbhjkla"


def count_occurrences(string):
    counter = collections.Counter(string)
    print(counter)
    print(counter.most_common(10))
    print(counter.fromkeys)


def clear_counter():
    counter = collections.Counter()
    for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        counter[word] += 1

    print(counter)


def counter_substract():
    c = collections.Counter(a=4, b=2, c=0, d=-2)
    d = collections.Counter(a=1, b=2, c=3, d=4)
    c.subtract(d)
    print(c)

def counter_total():
    c = collections.Counter(a=4, b=2, c=0, d=-2)
    print(c.total())
    print(c)

if __name__ == '__main__':
    dd = collections.defaultdict(list)
    dd['a'].append(1)  # Автоматически создает []
    print(dd)
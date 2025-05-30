"""
Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна определить, является ли данная скобочная последовательность правильной.

    Пустая последовательность явлется правильной.
    Если A — правильная последовательность, то последовательности (A), [A], {A} — правильные.
    Если A и B — правильные последовательности, то последовательность AB — правильная.

Формат ввода

В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.
Формат вывода

Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.
"""

def main():
    inpt = input().strip()
    stack = []
    bracket_p = {')': '(', ']': '[', '}': '{'}

    for char in inpt:
        if char in bracket_p.values():
            stack.append(char)
        elif char in bracket_p.keys():
            if not stack or stack[-1] != bracket_p[char]:
                print('no')
                return
            stack.pop()
    print('yes' if not stack else 'no')


if __name__ == '__main__':
    main()

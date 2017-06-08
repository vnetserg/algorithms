#!/usr/bin/env python3
'''
    https://www.hackerrank.com/challenges/marcs-cakewalk
'''


def min_miles(cakes):
    '''
        Вернуть минимальное количество миль, которое Марку придется пройти.
        Параметры:
            cakes - список количества калорий, где i-й элемент обозначает
                    количество колорий i-го пирожного
    '''
    return 0


def main():
    n_cakes = int(input().strip())
    cakes = [int(x) for x in input().split()]
    print(min_miles(cakes))


if __name__ == "__main__":
    main()

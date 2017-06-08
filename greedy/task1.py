#!/usr/bin/env python3
'''
    https://www.hackerrank.com/challenges/mark-and-toys
'''


def max_toys(money, toy_price):
    '''
        Вернуть максимальное количество игрушек, которые Марк сможет купить.
        Параметры:
            money - количество денег у Марка (int)
            toy_price - список цен игрушек
    '''
    return 0


def main():
    total_toys, money = [int(x) for x in input().split()]
    toy_price = [int(x) for x in input().split()]
    print(max_toys(money, toy_price))


if __name__ == "__main__":
    main()

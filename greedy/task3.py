#!/usr/bin/env python3
'''
    https://www.hackerrank.com/challenges/luck-balance
'''


def max_luck(max_loses, contests):
    '''
        Вернуть максимальное количество удачи, которое Лена может иметь
        после окончания всех контестов.
        Параметры:
            max_loses - максимальнок число важных контестов,
                    которые Лена может проиграть;
            contests - список кортежей (luck_balance, is_important)
    '''
    return 0


def main():
    n_contests, max_loses = [int(x) for x in input().split()]
    contests = [[int(x) for x in input().split()] for _ in range(n_contests)]
    print(max_luck(max_loses, contests))


if __name__ == "__main__":
    main()

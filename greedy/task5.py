#!/usr/bin/env python3
'''
    https://www.hackerrank.com/challenges/chief-hopper
'''


def min_energy(heights):
    '''
        Вернуть минимальное количество энергии, которое потребуется роботу.
        Параметры:
            heights - список высот зданий (int)
    '''
    return 0


def main():
    n = int(input().strip())
    heights = [int(x) for x in input().split()]
    print(min_energy(heights))


if __name__ == "__main__":
    main()

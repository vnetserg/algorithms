#!/usr/bin/env python3
'''
    https://www.hackerrank.com/challenges/quicksort1
'''


def partition(array):
    '''
        Вернуть массив, где сначала идут элементы, меньшие array[0],
        потом равные array[0], затем большие array[0].
        Параметры:
            array — список целых чисел
    '''
    return []


def main():
    n = int(input().strip())
    array = [int(x) for x in input().split()]
    print(" ".join(str(x) for x in partition(array)))


if __name__ == "__main__":
    main()

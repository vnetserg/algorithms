#!/usr/bin/env python3
'''
    https://www.hackerrank.com/challenges/pylons
'''


def min_towers(tower_range, city_towers):
    '''
        Вернуть минимальное количество вышек, которое придется включить
        для того, чтобы обеспечить электричеством все города.
        Если невозможно, вернуть -1.
        Параметры:
            tower_range - радиус действия вышки (электричеством обеспечиваются
                    все города, находящиеся БЛИЖЕ этого радиуса)
            city_towers - список количеств вышек в каждом городе (0 или 1)
    '''
    return 0


def main():
    n_cities, tower_range = [int(x) for x in input().split()]
    city_towers = [int(x) for x in input().split()]
    print(min_towers(tower_range, city_towers))


if __name__ == "__main__":
    main()

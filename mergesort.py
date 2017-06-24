#!/usr/bin/env python3

def merge_sort(array, lo, hi):
    if lo >= hi:
        return

    mid = (lo+hi)//2
    merge_sort(array, lo, mid)
    merge_sort(array, mid+1, hi)

    aux = merge(array, lo, mid, hi)
    for i, x in enumerate(aux):
        array[lo+i] = x


def merge(array, lo, mid, hi):
    aux = []
    i = lo
    k = mid+1

    while i <= mid and k <= hi:
        if array[i] < array[k]:
            aux.append(array[i])
            i += 1
        else:
            aux.append(array[k])
            k += 1

    aux += array[i:mid+1]
    aux += array[k:hi+1]

    return aux


def main():
    array = [int(x) for x in input().split()]
    merge_sort(array, 0, len(array)-1)
    print(" ".join(str(x) for x in array))


if __name__ == "__main__":
    main()

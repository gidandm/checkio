# -*- coding: utf-8 -*-
def checkio(data):
    data.sort()
    length = len(data)
    half = length//2
    if (length % 2) != 0:
        mediana = data[half]
    else:
        mediana = (data[(half)-1] + data[(half)])/2
    return mediana
# BEST
# off = len(data) // 2
# data.sort()
# med = data[off] + data[-(off + 1)]
# return med / 2

if __name__ == '__main__':
    print(checkio([1, 2, 3, 4, 5]))
    print(checkio([3, 1, 2, 5, 3]))
    print(checkio([1, 300, 2, 200, 1]))
    print(checkio([3, 6, 20, 99, 10, 15]))

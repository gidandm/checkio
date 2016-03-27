# -*- coding: utf-8 -*-
def checkio(data):
    result = []
    for i in range(len(data)):
        countf = 0
        for j in range(len(data)):
            if data[i] == data[j]:
                countf += 1
                if countf == 2:
                    result.append(data[i])
                    break
    return result
# BEST
# checkio=lambda d:[x for x in d if d.count(x)>1]



if __name__ == '__main__':
    print(checkio([1, 2, 3, 1, 3]))
    print(checkio([1, 2, 3, 4, 5]))
    print(checkio([5, 5, 5, 5, 5]))
    print(checkio([10, 9, 10, 10, 9, 8]))

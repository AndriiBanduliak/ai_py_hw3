import random as r


def getList(size):
    if size < 0:
        size = -size
    result = [0.0] * size
    for i in range(size):
        result[i] = round(r.uniform(0, 1000), 4)
    print(result)
    return result


def minMax(List):
    min = List[0] - List[0] // 1
    max = min
    for i in range(len(List)):
        fract = List[i] - List[i] // 1
        if fract > max:
            max = fract
        if fract < min:
            min = fract
    print(f' Minimum fractional part:{round(min, 4)}\n',
          
          f'Maximum fractional part: {round(max, 4)}\n ',
          
          end='')
    return round(max - min, 4)


print('Difference: ',
      minMax(getList(int(input('Enter the size of the list: ')))))

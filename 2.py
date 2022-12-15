from random import sample as sam


def SumList(List):
    sum = [0]
    for i in range(len(List) // 2):
        sum.append(List[i] * List[len(List) - i - 1])
    if not len(List) % 2 == 0:
        sum.append(List[len(List) - len(List) // 2 - 1])
    sum.remove(0)
    return sum


digits = list(sam(range(10), 10))
print(digits)
print(SumList(digits))
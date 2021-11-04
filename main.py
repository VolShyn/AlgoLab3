from collections import deque

data = []
emptytestlist = []

def add(value):
    return data.append(value)


def remove(value):
    try:
        data.remove(value)
    except ValueError:
        print('No such value')


if __name__ == '__main__':
    add(1), add(2), add(3), add(4), add(5)
    if data == emptytestlist:
        raise Exception('Data list is empty!')
    else:
        d = deque(data)
    Q = int(input('Print your Q: '))
    fleft = 0
    fright = 0
    for item in d:
        if item < Q:
            fleft += 1
        else:
            fright += 1
    n = iter(d)
    if fleft < fright:
        print('It would be better to take it from left side')
        for i in range(fleft+1):
            print(str(next(n)) + ' - ' + str(n))
    else:
        d.reverse()
        print('It would be better to take it from right side')
        for i in range(fright):
            print(str(next(n)) + ' - ' + str(n))

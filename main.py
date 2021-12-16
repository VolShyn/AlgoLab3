import random
from collections import deque
import PySimpleGUI as sg

data = []
emptytestlist = []


def add(value):
    return data.append(value)


def remove(value):
    try:
        data.remove(value)
    except ValueError:
        sg.popup_error('No such value')


if __name__ == '__main__':
    # add(1), add(2), add(3), add(4), add(5)

    for i in range(0, 100):
        add(i)

    if data == emptytestlist:
        sg.popup_error('Data list is empty!')
    else:
        d = deque(data)
    sg.theme('BluePurple')

    layout = [[sg.Text('Type your Q value:')],
              [sg.Input(key='-IN-')],
              [sg.Button('Show'), sg.Button('Exit')]]

    window = sg.Window('Pattern 2B', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            Q = int(values['-IN-'])
            fleft = 0
            for item in d:
                if item != Q:
                    fleft += 1
                else:
                    break
            if fleft == len(d):
                sg.popup_error('No such value')
                continue
            fright = len(data) - fleft
            print(fright)
            print(fleft)
            n = iter(d)
            if fleft < fright:
                sg.Print('It would be better to take it from left side')
                for i in range(fleft + 1):
                    sg.Print(str(i) + ' - ' + 'value: ' + str(next(n)) + ' - ' + str(n))
                    fleft = 0
                    fright = 0
            else:
                sg.Print('It would be better to take it from right side')
                for i in range(fright):
                    sg.Print(str(i) + ' - ' + 'value: ' + str(next(n)) + ' - ' + str(n))
                    fright = 0
                    fleft = 0

    window.close()
    # print(data[random.randint(0, 100)])
    # Q = int(input('Print your Q: '))
    # fleft = 0
    # for item in d:
    #     if item != Q:
    #         fleft += 1
    #     else:
    #         break
    # if fleft == len(d):
    #     raise Exception('No such value')

# fright = len(data) - fleft
# n = iter(d)
# if fleft < fright:
#     print('It would be better to take it from left side')
#     for i in range(fleft + 1):
#         print(str(i) + ' - ' + 'value: ' + str(next(n)) + ' - ' + str(n))
# else:
#     d.reverse()
#     print('It would be better to take it from right side')
#     for i in range(fright):
#         print(str(i) + ' - ' + 'value: ' + str(next(n)) + ' - ' + str(n))

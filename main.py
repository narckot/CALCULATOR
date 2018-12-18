from square import square
from calculator import calculator

print('\nПривет!')


def choice():  # ф-ция с выводом меню
    restart = True
    while restart:
        choise = input('\nВыбирете нужныю пункт из меню:\n'
                       '------------------------------\n'
                       'Калькулятор - (1)\n'
                       'Квадратный корень - (2)\n'
                       'Выход - (3)\n'
                       '------------------------------\n'
                       '>>> ')
        if len(choise) == 0:
            print('\nВы ввели символ не из списка...')
            continue
        if choise == '1':
            print('\nДобро пожаловать в калькулятор!\n')
            calculator()
        elif choise == '2':
            square()
        elif choise == '3':
            return
        else:
            print(
                '\n-----------ОШИБКА-----------\nВы ввели символ не из списка.\nПерезагрузка.\n---------------------------')
            restart = True


choice()

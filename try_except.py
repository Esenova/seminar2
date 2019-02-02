num_1 = input('Please, enter the 1 num: ')
num_2 = input('Please, enter the 2 num: ')

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print('Result of division is: ', num_1 / num_2)
except TypeError:
    print('TypeError: Can not make it int ')
    pass
except ValueError:
    print('ValueError: please enter the number')
    pass
except ZeroDivisionError:
    print('ZeroDivisionError: Can not delete to 0')
    pass

def some_func(number = input('Введите число ')):
    if number.find('.') == -1:
        return f'Число целое'
    else:
        a, b = number.split('.')
        if a == b:
            return True
        else:
            return False

print(some_func())
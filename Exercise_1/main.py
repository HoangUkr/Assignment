#функція обчислення добутку двох числа з використанням функції добутку
def multiplication(a,b):
    return a*b

#функція обчислення добутку двох числа ,без використання функції добутку
def exercise_1(a,b):
    res = 0
    if(a == 0 or b == 0):
        return 0
    else:
        for x in range(b):
            res = res + a
        return res

#функція перевірка результату
def checking(a,b):
    if(a == b):
        print('Correct')
    else:
        print('Wrong')


print('Enter number a: ')
a = int(input())

print('Enter number b: ')
b = int(input())

print('a * b = ', exercise_1(a,b))
checking(exercise_1(a,b), multiplication(a,b))




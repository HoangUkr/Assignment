from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'page/main.html')

def multiply(request):
    num_A = int(request.GET['number_a'])
    numb_B = int(request.GET['number_b'])
    res = exercise_2(num_A, numb_B)
    return render(request, 'page/result.html', {'result':res})

#функція обчислення добутку двох числа ,без використання функції добутку
def exercise_2(a,b):
    res = 0
    if(a == 0 or b == 0):
        return 0
    else:
        for x in range(b):
            res = res + a
        return res


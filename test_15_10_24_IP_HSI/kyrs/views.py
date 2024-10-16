from django.shortcuts import render
from datetime import datetime
import requests
from .models import Kyrs
import pytz



def priverka_intertvala(a, b, interval=10):
    'проверка того, прошло ли определённое интервалом количество секунд'
    c = (a - b).seconds
    if c >= interval:
        return True
    else:
        return False


def zapros_inf_o_kyrse():
    'запрос информации о курсе'
    inf = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    kyrs = inf['Valute']['USD']['Value']
    data_vrem = datetime.now(pytz.utc)
    return [data_vrem, kyrs]


def inf_iz_baz():
    'вывод информации из базы.'
    baz = Kyrs.objects.all()
    l, b1 = 0, []
    for i in baz:
        if l < 10:
            b1.append(i.kyrs)
            l += 1
        else:
            break
    return b1


def inf_v_baz():
    'отправка новой информации о курсе, в базу'
    k = zapros_inf_o_kyrse()
    dopolnenie = Kyrs(data_vrem=k[0], kyrs=k[1])
    dopolnenie.save()


def home(request):
    'стартовыя страница'
    return render(request, 'kyrs/kyrs.html')


def kyrs(request):
    'вывод значений курса'
    context = dict()
    ne_pysto = Kyrs.objects.all()
    if len(ne_pysto) == 0:   # для сутуации, когда в базе нет значений
        inf_v_baz()
    else:
        posled_zapis = Kyrs.objects.all().last()
        if priverka_intertvala(datetime.now(pytz.utc), posled_zapis.data_vrem):
            inf_v_baz()
    context['a'] = inf_iz_baz()
    return render(request, 'kyrs/kyrs.html', context)


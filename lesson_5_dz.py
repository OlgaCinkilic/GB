# -*- coding: utf-8 -*-

"""
1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

with open('lesson_5_dz_1.txt', 'w+') as my_f:
    text = input('Введите текст: ')
    while text:
        my_f.writelines(f"{text}\n")
        text = input('Введите текст: ')
        if not text:
            break
    my_f.seek(0)
    content = my_f.read()
    print(content)







"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, 
выполнить подсчёт строк и слов в каждой строке.
"""

with open("lesson_5_dz_2.txt", "r", encoding = 'utf-8') as f:
    cont = f.read()
    print(f'содержимое файла: \n{cont}')
    f.seek(0)
    lines = f.readlines()
    print(f'количество строк: {len(lines)}')
    f.seek(0)
    for i in range(len(lines)):
        line = f.readline()
        words = line.split()
        print(f'количество слов в {i + 1}-ой строке: {len(words)}')



"""
3. Создать текстовый файл (не программно). 
Построчно записать фамилии сотрудников и величину их окладов 
(не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тысяч, 
вывести фамилии этих сотрудников. 
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open("lesson_5_dz_3.txt", "rt", encoding='utf-8') as f:
    cont = f.readlines()
    f.seek(0)
    sal = []
    for i in range(len(cont)):
        line = f.readline()
        words = line.split()
        if float(words[1]) < 20000:
            print(words[0])
        sal.append(words[1])
    print(f'средний доход сотрудников: {sum(map(float, sal)) / len(sal)}')


"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open("lesson_5_dz_4.txt", "r", encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(dict[i[0]] + '  ' + i[1])
with open('lesson_5_dz_4_2.txt', 'w+', encoding='utf-8') as f2:
    f2.writelines(new_file)
    f2.seek(0)
    cont2 = f2.read()
    print(cont2)




"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""


def summary():
    with open("lesson_5_dz_5.txt", "w+") as f:
        line = input('введите числа через пробел : ')
        f.writelines(line)
        num = line.split()
        print(sum(map(float, num)))
summary()





"""
6. Сформировать (не программно) текстовый файл. 
В нём каждая строка должна описывать учебный предмет и наличие лекционных, 
практических и лабораторных занятий по предмету. 
Сюда должно входить и количество занятий. 
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество 
занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

file = open("lesson_5_dz_6.txt", encoding='utf-8')
onstring = file.read().split("\n")[:-1]
print(onstring)

dict = {}

for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value
print(dict)

print("\n Общее количество занятий по предметам ")
for i in dict:
    list = dict[i]
    summ = 0
    for j in range(0, len(list)):
        summ += int(list[j])
    print(i, ":", summ)
file.close()





"""
7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка будет содержать данные о фирме: название, 
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, 
в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. Если фирма получила убытки, 
также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('lesson_5_dz_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, form_ownership, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Компании работают в убыток')
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль компаний - {profit}')

with open('lesson_5_dz_7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json с содержимым: \n'
          f'{js_str}')
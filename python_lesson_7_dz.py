# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 18:10:26 2022

@author: 79264
"""
"""
1. Реализовать класс Matrix (матрица). 
Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, 
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() 
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() 
для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: 
сложение элементов матриц выполнять поэлементно — первый элемент первой строки
 первой матрицы складываем с первым элементом 
 первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, data:list):
        self.data = data

    def __str__(self):
        result = []
        for row in self.data:
            result.append(' '.join([str(k) for k in row]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.data) == len(other.data):
            result = []
            for i, row in enumerate(self.data):
                new_list = list(map(lambda x, y: x + y, row, other.data[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return



list_lists_01 = [[33, 22, 44], [30, 3, 43], [40, 13, 22]]
list_lists_02 = [[2, 4, 6], [4, 3, 3], [1, 3, 2]]

matrix01 = Matrix(list_lists_01)
matrix02 = Matrix(list_lists_02)
matrix03 = matrix01 + matrix02

print(matrix01, end='\n\n')
print(matrix02, end='\n\n')
print(matrix03)



"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, 
которая может иметь определённое название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) 
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: 
    для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 
Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта, 
    проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class WorkingForm(ABC):
    @abstractmethod
    def fabric_calculation(self):
        pass


class Coat(WorkingForm):
    def __init__(self, v):
        self.v = v
    @property
    def fabric_calculation(self):
        V = self.v/6.5 + 0.5
        return f'Ткани понадобится на пальто: {V}'


class Suite(WorkingForm):
    def __init__(self, h):
        self.h = h
    @property
    def fabric_calculation(self):
        H = 2*self.h + 0.3
        return f'Ткани понадобится на костюм: {H}'
    
    
class TotalFabric(WorkingForm):
    def __init__(self, v, h):
        self.V = v
        self.H = h

    @property
    def fabric_calculation(self):
        all = (self.V/6.5 + 0.5) + (2*self.H + 0.3)
        return f'Всего ткани понадобится: {all}'


coat = Coat(69)
suite = Suite(205)
total = TotalFabric(45, 235)
print(suite.fabric_calculation)
print(coat.fabric_calculation)
print(total.fabric_calculation)




"""
3. Реализовать программу работы с органическими клетками, 
состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, 
соответствующий количеству ячеек клетки (целое число).
 В классе должны быть реализованы методы перегрузки арифметических операторов:
     сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
     деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
 соответственно.
Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек
исходных двух клеток.
Вычитание. Участвуют две клетки. 
Операцию необходимо выполнять только если разность количества ячеек двух клеток 
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки 
определяется как произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется 
как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), 
принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., 
где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, 
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
       

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
       return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

        
    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(22)
cells2 = Cell(2)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)





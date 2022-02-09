# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:34:18 2022

@author: 79264
"""
"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы:
    красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, 
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке
 (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. 
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color = color
    def running(self):
        for key, value in self.__color.items():
            sleep(value)
            print(key)


traf = TrafficLight(color={"Красный": 7,"Желтый": 2,"Зеленый": 10})
traf.running()


"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного 
кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.thickness = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.thickness / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')


r = Road(5000, 20)
r.asphalt_mass()



"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, 
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника 
(get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры 
класса Position, передать данные, проверить значения атрибутов, 
вызвать методы экземпляров.
"""
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
        


a = Position('Шерлок', 'Хомс', 'Детектив', 200000, 55000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())



"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, 
is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат.
"""

class Car:
  
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} движется'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} поворот на право'

    def turn_left(self):
        return f'{self.name} поворот на лево'

    def show_speed(self):
        return f'Скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name}  выше, чем допустимо для городского автомобиля'
        else:
            return f'У {self.name} допустимая скорость для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость у рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f' Скорость {self.name} выше, чем допустимо для рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} это не полицейская машина'


audi = SportCar(100, 'черный', 'Audi', False)
peugeot = TownCar(75, 'белый', 'Peugeot', False)
vw = WorkCar(70, 'синий', 'Volkswagen', False)
ford = PoliceCar(110, 'белый',  'Ford', True)
print(vw.turn_left())
print(f'{peugeot.turn_right()}, а {audi.stop()}')
print(f'{vw.go()} со скоростью {vw.show_speed()}')
print(f'{vw.name}  {vw.color}')
print(f' {audi.name} - полицейская машина? {audi.is_police}')
print(f' {vw.name}  - полицейская машина? {vw.is_police}')
print(audi.show_speed())
print(peugeot.show_speed())
print(ford.police())
print(ford.show_speed())



"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. 
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, 
что выведет описанный метод для каждого экземпляра.
"""

class Stationary:
    
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())

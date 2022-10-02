from homework_02.base import Vehicle
from homework_02.engine import Engine
"""
создайте класс `Car`, наследник `Vehicle`
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает в себя 
экземпляр объекта Engine и устанавливает на текущий экземпляр Car
"""


class Car(Vehicle):
    engine: Engine = None

    def set_engine(self, engine):
        self.engine = engine

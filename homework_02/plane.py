from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


"""
создайте класс `Plane`, наследник `Vehicle`
обавьте атрибуты `cargo` и `max_cargo` классу `Plane`
добавьте `max_cargo` в инициализатор (переопределите родительский)
объявите метод `load_cargo`, который принимает число, проверяет, 
что в сумме с текущим `cargo` не будет перегруза, и обновляет значение,
в ином случае выкидывает исключение `exceptions.CargoOverload`
объявите метод `remove_all_cargo`, который обнуляет значение `cargo` 
и возвращает значение `cargo`, которое было до обнуления
"""

class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, load):
        if load + self.cargo <= self.max_cargo:
            self.cargo = load + self.cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp


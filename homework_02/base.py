from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int
    fuel: int
    started = False
    fuel_consumption: int

    def __init__(self, weight=750, fuel=20, fuel_consumption=5):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0 & self.started != True:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance):
        if self.fuel / self.fuel_consumption >= distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel

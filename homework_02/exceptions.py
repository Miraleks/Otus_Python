"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __str__(self):
        return 'Low fuel'

class NotEnoughFuel(Exception):
    def __str__(self):
        return 'Not enough fuel'

class CargoOverload(Exception):
    def __str__(self):
        return 'Over load'

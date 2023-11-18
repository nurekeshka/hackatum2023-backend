from enum import Enum


class FluidConversions(Enum):
    to_litres = 1000
    to_tablespoon = 1 / 14.7868
    to_teaspoon = 1 / 5
    to_cup = 1 / 240


class MassConversions(Enum):
    to_kilograms = 1000
    to_tablespoon = 1 / 14.175
    to_teaspoon = 1 / 5
    to_cup = 1 / 240
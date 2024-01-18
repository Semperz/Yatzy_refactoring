from enum import IntEnum, unique

@unique
class Pips(IntEnum):
    ONE, TWO, THREE, FOUR, FIVE, SIX = range(1,7)

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]



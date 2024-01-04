from src.pips import Pips

class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != len(dice):
            return 0
        return 50

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    @staticmethod
    def fours(*dice):
        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(*dice):
        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE

    @staticmethod
    def sixes(*dice):
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX

    @staticmethod
    def pair(*dice):
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) >= PAIR:
                return PAIR * pip
        return 0

    @classmethod
    def two_pairs(cls, *dice):
        PAIR = 2
        pips_pairs = cls.__filter_pips_repeated(dice, PAIR)
        return sum(pips_pairs) * PAIR if len(pips_pairs) == 2 else 0

    @classmethod
    def three_of_a_kind(cls, *dice):
        THREE = 3
        pip = cls.__biggest_pip_repeated(dice, THREE)
        return pip * THREE if pip else 0

    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR = 4
        pip = cls.__biggest_pip_repeated(dice, FOUR)
        return pip * FOUR if pip else 0

    @classmethod
    def __biggest_pip_repeated(cls, dice, times):
        pips = cls.__filter_pips_repeated(dice, times)
        return pips[0] if pips else []

    @classmethod
    def __filter_pips_repeated(cls, dice, times):
        return list(filter(lambda pip: dice.count(pip) >= times, Pips.reversedValues()))

    @classmethod
    def small_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else 0

    @classmethod
    def large_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else 0

    @classmethod
    def full_house(cls, *dice):
        if cls.two_of_a_kind(*dice) and cls.three_of_a_kind(*dice):
            return cls.two_of_a_kind(*dice) + cls.three_of_a_kind(*dice)
        else:
            return 0

    @classmethod
    def two_of_a_kind(cls, *dice):
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) == PAIR:
                return PAIR * pip
        return 0

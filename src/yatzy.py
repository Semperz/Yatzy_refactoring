class Yatzy:

    @staticmethod
    def chance(*dices):
        total = sum(dices)
        return total

    @staticmethod
    def yatzy(*dices):
        if dices.count(dices[0]) != len(dices):
            return 0
        else:
            return 50

    @staticmethod
    def ones(*dices):
        ones_sum = 0
        for ones in dices:
            if ones == 1:
                ones_sum += 1
        return ones_sum

    @staticmethod
    def twos(*dices):
        twos_sum = 0
        for twos in dices:
            if twos == 2:
                twos_sum += 2
        return twos_sum
    @staticmethod
    def threes(*dices):
        threes_sum = 0
        for threes in dices:
            if threes == 3:
                threes_sum += 3
        return threes_sum
    @staticmethod
    def fours(*dices):
        fours_sum = 0
        for fours in dices:
            if fours == 4:
                fours_sum += 4
        return fours_sum

    @staticmethod
    def fives(*dices):
        fives_sum = 0
        for fives in dices:
            if fives == 5:
                fives_sum += 5
        return fives_sum

    @staticmethod
    def sixes(*dices):
        sixes_sum = 0
        for sixes in dices:
            if sixes == 6:
                sixes_sum += 6
        return sixes_sum

    @staticmethod
    def score_pair(*dices):
        for pairs in range(6,0,-1):
            if dices.count(pairs) == 2:
                return pairs * 2
        return 0


    @staticmethod
    def two_pair(*dices):
        double_pair = set()
        for pairs in range(6, 0, -1):
            double_pair_count = dices.count(pairs)
            if double_pair_count >= 2:
                double_pair.add(pairs * 2)
        if len(double_pair) >= 2:
            return sum(double_pair)
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def small_straight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def large_straight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def full_house(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
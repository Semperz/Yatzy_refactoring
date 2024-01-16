class Yatzy:

    @staticmethod
    def chance(*dices):
        '''
        Before refactor: Code is duplicated and function takes too many parameters
        '''
        total = sum(dices)
        return total

    @staticmethod
    def yatzy(*dices):
        '''
        Before refactor: A loop is too long and too deeply nested
        '''
        if dices.count(dices[0]) != len(dices):
            return 0
        else:
            return 50

    @staticmethod
    def ones(*dices):
        '''
        Before refactor: Code is duplicated and function takes too many parameters
        '''
        ones_sum = 0
        for ones in dices:
            if ones == 1:
                ones_sum += 1
        return ones_sum

    @staticmethod
    def twos(*dices):
        '''
        Before refactor: Code is duplicated and function takes too many parameters
        '''
        twos_sum = 0
        for twos in dices:
            if twos == 2:
                twos_sum += 2
        return twos_sum
    @staticmethod
    def threes(*dices):
        '''
        Before refactor: Code is duplicated and function takes too many parameters
        '''
        threes_sum = 0
        for threes in dices:
            if threes == 3:
                threes_sum += 3
        return threes_sum
    @staticmethod
    def fours(*dices):
        '''
        Before refactor: A routine uses more features of another class than of its own class
        '''
        fours_sum = 0
        for fours in dices:
            if fours == 4:
                fours_sum += 4
        return fours_sum

    @staticmethod
    def fives(*dices):
        '''
        Before refactor: A routine uses more features of another class than of its own class
        '''
        fives_sum = 0
        for fives in dices:
            if fives == 5:
                fives_sum += 5
        return fives_sum

    @staticmethod
    def sixes(*dices):
        '''
        Before refactor: A routine uses more features of another class than of its own class
        '''
        sixes_sum = 0
        for sixes in dices:
            if sixes == 6:
                sixes_sum += 6
        return sixes_sum

    @staticmethod
    def score_pair(*dices):
        '''
        Before refactor: A chain of routines passes tramp data
                         Code is duplicated and function takes too many parameters
        '''
        for pairs in range(6,0,-1):
            if dices.count(pairs) >= 2:
                return pairs * 2
        return 0


    @staticmethod
    def two_pair(*dices):
        '''
        Before refactor: A chain of routines passes tramp data
                         Code is duplicated and function takes too many parameters
        '''
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
    def four_of_a_kind(*dices):
        '''
        Before refactor: A chain of routines passes tramp data
                         Code is duplicated and function takes too many parameters
        '''
        for num_fours in range(6, 0, -1):
            if dices.count(num_fours) >= 4:
                return num_fours * 4
        return 0

    @staticmethod
    def three_of_a_kind(*dices):
        '''
        Before refactor: A chain of routines passes tramp data
                         Code is duplicated and function takes too many parameters
        '''
        for num_threes in range(6, 0, -1):
            if dices.count(num_threes) >= 3:
                return num_threes * 3
        return 0

    @staticmethod
    def small_straight(*dices):
        '''
        Before refactor: A chain of routines passes tramp data
                         Code is duplicated and function takes too many parameters
        '''
        if tuple(sorted(dices)) == (1,2,3,4,5):
            return 15
        return 0

    @staticmethod
    def large_straight(*dices):
        '''
        Before refactor: A chain of routines passes tramp data
                         Code is duplicated and function takes too many parameters
        '''
        if tuple(sorted(dices)) == (2,3,4,5,6):
            return 20
        return 0
    @staticmethod
    def full_house(*dices):
        '''
        Before refactor: A loop is too long or too deeply nested
                         Function takes too many parameters
        '''
        dictionary = {}
        final_score = 0
        for number in dices:
            if number not in dictionary:
                dictionary[number] = dices.count(number)
        if len(dictionary) != 2:
            return 0
        if 2 in dictionary.values() and 3 in dictionary.values():
            lista = list(dictionary.items())
            if lista[0][1] == 2:
                final_score += lista[0][0] * 2
            else:
                final_score += lista[0][0] * 3
            if lista[1][1] == 2:
                final_score += lista[1][0] * 2
            else:
                final_score += lista[1][0] * 3
        return final_score
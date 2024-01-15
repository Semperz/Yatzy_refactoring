from src.yatzy import Yatzy
import pytest

@pytest.mark.chance
def test_chance_all_dice_sum():
    expected = 15
    actual = Yatzy.chance(2, 3, 4, 5, 1)
    assert expected == actual
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)
    assert 30 == Yatzy.chance(6, 6, 6, 6, 6)
    assert 12 == Yatzy.chance(2, 3, 1, 1, 5)
    assert 5 == Yatzy.chance(1, 1, 1, 1, 1)
    assert 19 == Yatzy.chance(5, 4, 3, 3, 4)

@pytest.mark.yatzy
def test_yatzy_scores_50():
    expected = 50
    actual = Yatzy.yatzy(4, 4, 4, 4, 4)
    assert expected == actual
    assert 50 == Yatzy.yatzy(6, 6, 6, 6, 6)
    assert 50 == Yatzy.yatzy(2, 2, 2, 2, 2)
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(6, 6, 6, 6, 3)
    assert 0 == Yatzy.yatzy(2, 1, 2, 1, 2)
    assert 0 == Yatzy.yatzy(1, 2, 5, 4, 2)
    assert 0 == Yatzy.yatzy(4, 4, 5, 5, 5)

@pytest.mark.ones
def test_ones():
    assert Yatzy.ones(1, 2, 3, 4, 5) == 1
    assert 0 == Yatzy.ones(6, 2, 2, 4, 5)
    assert 0 == Yatzy.ones(4, 4, 4, 4, 4)
    assert 1 == Yatzy.ones(6, 2, 3, 5, 1)
    assert 2 == Yatzy.ones(1, 2, 1, 4, 5)
    assert 3 == Yatzy.ones(2, 1, 4, 1, 1)
    assert 4 == Yatzy.ones(1, 2, 1, 1, 1)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)

@pytest.mark.twos
def test_twos():
    assert 0 == Yatzy.twos(6, 1, 5, 3, 4)
    assert 2 == Yatzy.twos(2, 4, 4, 3, 5)
    assert 4 == Yatzy.twos(1, 2, 3, 2, 6)
    assert 6 == Yatzy.twos(2, 5, 2, 3, 2)
    assert 8 == Yatzy.twos(2, 2, 1, 2, 2)
    assert 10 == Yatzy.twos(2, 2, 2, 2, 2)


@pytest.mark.threes
def test_threes():
    assert 0 == Yatzy.threes(1, 2, 4, 2, 4)
    assert 3 == Yatzy.threes(1, 2, 3, 2, 5)
    assert 6 == Yatzy.threes(1, 2, 3, 2, 3)
    assert 9 == Yatzy.threes(3, 2, 3, 2, 3)
    assert 12 == Yatzy.threes(2, 3, 3, 3, 3)
    assert 15 == Yatzy.threes(3, 3, 3, 3, 3)

@pytest.mark.fours
def test_fours():
    assert 20 == Yatzy.fours(4, 4, 4, 4, 4)
    assert 16 == Yatzy.fours(4, 4, 1, 4, 4)
    assert 12 == Yatzy.fours(4, 4, 4, 5, 5)
    assert 8 == Yatzy.fours(4, 4, 5, 5, 5)
    assert 4 == Yatzy.fours(4, 5, 5, 5, 5)
    assert 0 == Yatzy.fours(3, 2, 1, 6, 6)
    assert 0 == Yatzy.fours(1, 2, 3, 5, 6)

@pytest.mark.fives
def test_fives():
    assert 0 == Yatzy.fives(3, 3, 3, 3, 3)
    assert 0 == Yatzy.fives(4, 1, 4, 2, 6)
    assert 5 == Yatzy.fives(6, 4, 2, 2, 5)
    assert 10 == Yatzy.fives(1, 3, 4, 5, 5)
    assert 15 == Yatzy.fives(6, 4, 5, 5, 5)
    assert 20 == Yatzy.fives(4, 5, 5, 5, 5)
    assert 25 == Yatzy.fives(5, 5, 5, 5, 5)

@pytest.mark.sixes
def test_sixes():
    assert 0 == Yatzy.sixes(4, 4, 4, 5, 5)
    assert 6 == Yatzy.sixes(4, 4, 6, 5, 5)
    assert 12 == Yatzy.sixes(2, 1, 6, 6, 3)
    assert 18 == Yatzy.sixes(6, 5, 6, 6, 5)
    assert 24 == Yatzy.sixes(6, 1, 6, 6, 6)
    assert 30 == Yatzy.sixes(6, 6, 6, 6, 6)

@pytest.mark.pair
def test_one_pair():
    assert 0 == Yatzy.score_pair(1, 3, 2, 5, 6)
    assert 4 == Yatzy.score_pair(3, 4, 2, 5, 2)
    assert 6 == Yatzy.score_pair(3, 4, 3, 5, 6)
    assert 8 == Yatzy.score_pair(3, 4, 4, 5, 6)
    assert 8 == Yatzy.score_pair(3, 4, 2, 4, 2)
    assert 10 == Yatzy.score_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy.score_pair(5, 3, 6, 6, 5)

@pytest.mark.pairs
def test_two_pair():
    assert 0 == Yatzy.two_pair(3, 3, 6, 5, 4)
    assert 6 == Yatzy.two_pair(2, 2, 1, 1, 5)
    assert 10 == Yatzy.two_pair(3, 2, 3, 2, 1)
    assert 16 == Yatzy.two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy.two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy.two_pair(6, 6, 5, 6, 6)

@pytest.mark.three_kind
def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)
    assert 12 == Yatzy.three_of_a_kind(4, 4, 3, 4, 1)
    assert 18 == Yatzy.three_of_a_kind(6, 3, 6, 3, 6)
    assert 6 == Yatzy.three_of_a_kind(2, 2, 2, 2, 5)
    assert 3 == Yatzy.three_of_a_kind(1, 6, 1, 6, 1)

@pytest.mark.four_kind
def test_four_of_a_kind():
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)
    assert 24 == Yatzy.four_of_a_kind(6, 1, 6, 6, 6)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 3, 2, 2)
    assert 4 == Yatzy.four_of_a_kind(1, 5, 1, 1, 1)

@pytest.mark.small
def test_small_straight():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.small_straight(2, 3, 4, 5, 1)
    assert 15 == Yatzy.small_straight(1, 3, 5, 4, 2)
    assert 0 == Yatzy.small_straight(1, 2, 2, 4, 5)
    assert 0 == Yatzy.small_straight(1, 2, 6, 4, 5)
    assert 0 == Yatzy.small_straight(4, 2, 3, 1, 1)

@pytest.mark.large
def test_large_straight():
    assert 20 == Yatzy.large_straight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 20 == Yatzy.large_straight(6, 5, 4, 3, 2)
    assert 0 == Yatzy.large_straight(4, 2, 3, 1, 5)
    assert 0 == Yatzy.large_straight(6, 6, 4, 3, 2)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 5)

@pytest.mark.full_house
def test_full_house():
    assert 18 == Yatzy.full_house(6, 2, 2, 2, 6)
    assert 0 == Yatzy.full_house(2, 3, 4, 5, 6)
    assert 0 == Yatzy.full_house(2, 4, 4, 1, 2)
    assert 28 == Yatzy.full_house(6, 6, 6, 5, 5)
    assert 0 == Yatzy.full_house(1, 1, 2, 3, 2)
    assert 13 == Yatzy.full_house(1, 5, 1, 5, 1)
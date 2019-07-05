import pytest
from services.ScoreCandidate import ScoreCandidate


def test_calc_n_expected_result():
    candidate = ScoreCandidate()

    assert 75 == candidate.calc_n(5, 4)


def test_calc_score_expected_result():
    candidate = ScoreCandidate()

    assert 50 == candidate.calc_score(75, 25)


def test_cald_d_expected_result_better_way_from_a_to_b():
    candidate = ScoreCandidate()

    distance = candidate.calc_d("A", "B")

    assert 5 == distance['better_way']


def test_cald_d_expected_result_better_way_from_a_to_e():
    candidate = ScoreCandidate()

    distance = candidate.calc_d("A", "E")

    # assert 16 == distance['better_way']

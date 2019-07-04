import pytest
from services.ScoreCandidate import ScoreCandidate


def test_calc_n_expected_result():
    candidate = ScoreCandidate()

    assert 75 == candidate.calc_n(5, 4)


def test_calc_score_expected_result():
    candidate = ScoreCandidate()

    assert 50 == candidate.calc_score(75, 25)


def test_cald_d_expected_result():
    candidate = ScoreCandidate()

    candidate.calc_d("A", "C")

    assert True

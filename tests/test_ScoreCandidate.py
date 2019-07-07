import pytest
from services.ScoreCandidate import ScoreCandidate


def test_calc_n_expected_result():
    candidate = ScoreCandidate()

    assert 75 == candidate.calc_n(5, 4)


def test_calc_score_expected_result():
    candidate = ScoreCandidate()

    assert 50 == candidate.calc_score(75, 25)


def test_cald_d_expected_result_better_way_from_a_to_b():
    score = ScoreCandidate()

    assert 100 == score.calc_d("a", "b")


def test_cald_d_expected_result_better_way_from_a_to_e():
    score = ScoreCandidate()

    assert 25 == score.calc_d("a", "e")


def test_cald_d_expected_result_better_way_from_a_to_e():
    score = ScoreCandidate()

    assert 25 == score.calc_d("a", "f")

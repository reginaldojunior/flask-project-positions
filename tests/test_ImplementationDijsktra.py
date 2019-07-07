import pytest
from services.Dijsktra import Dijkstra


def test_cald_d_expected_result_better_way_from_a_to_b():
    dijkstra = Dijkstra(
        [
            ("a", "b", 5), ("b", "c", 7),
            ("b", "d", 3), ("c", "b", 7), ("c", "e", 4),  ("d", "e", 10),
            ("d", "f", 8)
        ]
    )

    assert 5 == dijkstra.dijkstra("a", "b")


def test_cald_d_expected_result_better_way_from_a_to_e():
    dijkstra = Dijkstra(
        [
            ("a", "b", 5), ("b", "c", 7),
            ("b", "d", 3), ("c", "b", 7), ("c", "e", 4),  ("d", "e", 10),
            ("d", "f", 8)
        ]
    )

    assert 8 == dijkstra.dijkstra("d", "a")


def test_cald_d_expected_result_better_way_from_a_to_e():
    dijkstra = Dijkstra(
        [
            ("a", "b", 5), ("b", "c", 7),
            ("b", "d", 3), ("c", "b", 7), ("c", "e", 4),  ("d", "e", 10),
            ("d", "f", 12)
        ]
    )

    assert 20 == dijkstra.dijkstra("a", "f")

from services.Dijsktra import Dijkstra


class ScoreCandidate:
    def calc_d(self, origin, destiny):
        dijkstra = Dijkstra(
            [
                ("a", "b", 5), ("b", "c", 7),
                ("b", "d", 3), ("c", "b", 7), ("c", "e", 4),  ("d", "e", 10),
                ("d", "f", 8)
            ]
        )

        return dijkstra.dijkstra(origin, destiny)

    def calc_n(self, nv, nc):
        return 100 - 25 * abs((nv - nc))

    def calc_score(self, n, d):
        return (n + d) / 2

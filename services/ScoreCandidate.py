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

        distance = dijkstra.dijkstra(origin.lower(), destiny.lower())

        if distance <= 5:
            return 100
        elif distance >= 5 and distance <= 10:
            return 75
        elif distance >= 10 and distance <= 15:
            return 50
        elif distance >= 15 and distance <= 20:
            return 25
        else:
            return 0

    def calc_n(self, nv, nc):
        return 100 - 25 * abs((nv - nc))

    def calc_score(self, n, d):
        return (n + d) / 2

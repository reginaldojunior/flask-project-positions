

class ScoreCandidate():

    LOCATIONS = {
        "A": {
            "B": 5
        },
        "B": {
            "A": 5,
            "C": 7,
            "D": 3
        },
        "C": {
            "B": 7,
            "E": 4
        },
        "D": {
            "B": 3,
            "E": 10,
            "F": 8
        },
        "E": {
            "C": 4,
            "D": 10
        },
        "F": {
            "D": 8
        }
    }

    def calc_n(self, nv, nc):
        return 100 - 25 * abs((nv - nc))

    def calc_score(self, n, d):
        return (n + d) / 2

    def calc_d(self, origin, destiny):
        last_local_passed = None
        next_ways_to_destiny = None

        better_way = self.find_better_way(self.LOCATIONS, origin, destiny)

        return {"better_way": better_way}

    def find_better_way(self, ways, origin, destiny):
        for name in ways:
            if (name == origin):
                return self.find_better_way_from_origin(ways, ways[name],
                                                        destiny)

    def find_better_way_from_origin(self, ways, start, destiny):
        distance_between_start_from_ways = 0
        for ways_possible_from_origin in start:
            if (ways_possible_from_origin == destiny):
                distance_between_start_from_ways = start[
                    ways_possible_from_origin
                ]

                break

            for name in ways:
                if (ways_possible_from_origin == name):
                    print(ways[ways_possible_from_origin])

        return distance_between_start_from_ways

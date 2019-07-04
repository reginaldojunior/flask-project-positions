

class ScoreCandidate():

    LOCATIONS = [
        {
            "A": {
                "B": 5
            },
        },
        {
            "B": {
                "A": 5,
                "C": 7,
                "D": 3
            },
        },
        {
            "C": {
                "B": 7,
                "E": 4
            },
        },
        {
            "D": {
                "B": 3,
                "E": 10,
                "F": 8
            },
        },
        {
            "E": {
                "C": 4,
                "D": 10
            },
        },
        {
            "F": {
                "D": 8
            }
        }
    ]

    def __init__(self):
        pass

    def calc_n(self, nv, nc):
        return 100 - 25 * abs((nv - nc))

    def calc_score(self, n, d):
        return (n + d) / 2

    def calc_d(self, location_a, location_b):
        last_local_passed = None

        for local in self.LOCATIONS:
            for name, distance in local.items():
                if (name == location_a):
                    print("\n")
                    print(distance)

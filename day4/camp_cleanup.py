import os

__location__ = os.path.dirname(os.path.realpath(__file__))
PAIR_ASSIGNMENTS = os.path.join(__location__, "pair_assignments.txt")

def make_interval(low_high_pair):
    return Interval(int(low_high_pair[0]), int(low_high_pair[1]))

class Interval():
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def contains(self, other) -> bool:
        return (self.low <= other.low) and (self.high >= other.high)

    def no_overlap(self, other):
        return (self.low > other.high) or (self.high < other.low)

def part_one(filepath):
    with open(filepath, "r") as file:
        overlapping_pairs = []
        for line in file.readlines():
            pair_one, pair_two = line.split(",")
            interval_one = make_interval(pair_one.split("-"))
            interval_two = make_interval(pair_two.split("-"))
            if interval_one.contains(interval_two) or interval_two.contains(interval_one):
                overlapping_pairs.append(line)
        print(len(overlapping_pairs))

def part_two(filepath):
    with open(filepath, "r") as file:
        overlapping_pairs = []
        total = 0
        for line in file.readlines():
            total += 1
            pair_one, pair_two = line.split(",")
            interval_one = make_interval(pair_one.split("-"))
            interval_two = make_interval(pair_two.split("-"))
            if interval_one.no_overlap(interval_two):
                overlapping_pairs.append(line)
        print(total - len(overlapping_pairs))

def main():
    part_one("/Users/andrewcooke/Documents/github/advent-of-code-2022/day4/test_input.txt")
    part_one(PAIR_ASSIGNMENTS)
    part_two(PAIR_ASSIGNMENTS)

if __name__ == "__main__":
    main()


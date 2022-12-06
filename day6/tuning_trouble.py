import os
from collections import Counter

__location__ = os.path.dirname(os.path.realpath(__file__))
PROCEDURE = os.path.join(__location__, "signal.txt")

def check_unique(str):
    return len(Counter(str)) == len(str)

def part_one(filepath):
    with open(filepath) as file:
        signal = file.readline().strip()
        for i in range(4, len(signal), 1):
            window = signal[i-4:i]
            if check_unique(window):
                print(i, window)
                break

def part_two(filepath):
    with open(filepath) as file:
        signal = file.readline().strip()
        for i in range(14, len(signal), 1):
            window = signal[i-14:i]
            if check_unique(window):
                print(i, window)
                break

def main():
    part_one(PROCEDURE)
    part_two(PROCEDURE)

if __name__ == "__main__":
    main()
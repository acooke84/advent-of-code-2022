import os

__location__ = os.path.dirname(os.path.realpath(__file__))
RUCKSACK_LIST = os.path.join(__location__, "rucksack_list.txt")

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def get_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

def part_one():
    with open(RUCKSACK_LIST, "r") as file:
        priority = 0
        for line in file:
            n = int((len(line) - 1)/2)
            sack_1, sack_2 = line[:n], line[n:-1]
            for c in sack_1:
                if c in sack_2:
                    priority += get_priority(c)
                    break
        print("PART 1: ", priority)

def part_two():
    with open(RUCKSACK_LIST, "r") as file:
        priority = 0
        for (sack_1, sack_2, sack_3) in chunker(file.readlines(), 3):
            for item in sack_1:
                if item in sack_2 and item in sack_3:
                    priority += get_priority(item)
                    break
        print("PART 2: ", priority)

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
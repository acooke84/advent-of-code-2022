import os
import re
from collections import namedtuple

__location__ = os.path.dirname(os.path.realpath(__file__))
PROCEDURE = os.path.join(__location__, "rearrangement_procedure.txt")

Move = namedtuple("Move", "count source target")

def moves_and_stacks(filepath):
    with open(filepath, "r") as file:
        line = file.readline()
        stacks = [[] for i in range(9)]
        while line.strip():
            x = 4
            stack = [re.sub(r'[^a-zA-Z]', '', line[y-x:y]) for y in range(x, len(line)+x,x)]
            for i, crate in enumerate(stack):
                if crate:
                    stacks[i].insert(0, crate)
            line = file.readline()
        moves = []
        line = file.readline()
        while line.strip():
            tokens = line.split()
            moves.append(Move(int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1))
            line = file.readline()
    return stacks, moves

def make_move(move: Move, stacks, crane=9000):
    if crane == 9000:
        for i in range(move.count):
            stacks[move.target].append(stacks[move.source].pop())
    else:
        cnt = move.count
        while cnt > 0:
            stacks[move.target].append(stacks[move.source].pop(-cnt))
            cnt -= 1
    return stacks

def make_message(stacks):
    message = ""
    for stack in stacks:
        message += stack[-1] if stack else ""
    return message

def part_one(filepath):
    stacks, moves = moves_and_stacks(filepath)
    for move in moves:
        stacks = make_move(move, stacks)
    message = make_message(stacks)
    print(message)

def part_two(filepath):
    stacks, moves = moves_and_stacks(filepath)
    for move in moves:
        stacks = make_move(move, stacks, 9001)
    message = make_message(stacks)
    print(message)

def main():
    part_one("/Users/andrewcooke/Documents/github/advent-of-code-2022/day5/test_procedure.txt")
    part_one(PROCEDURE)
    part_two("/Users/andrewcooke/Documents/github/advent-of-code-2022/day5/test_procedure.txt")
    part_two(PROCEDURE)

if __name__ == "__main__":
    main()

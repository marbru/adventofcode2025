#!/usr/bin/env python3
# https://adventofcode.com/2025/day/1

DEBUG = True
INPUT_FILE = "./input"

def test_move_dial():
    assert move_dial(50, "L", 68) == (82, 0)
    assert move_dial(50, "L", 30) == (20, 0)
    assert move_dial(50, "R", 48) == (98, 0)
    assert move_dial(50, "L", 5) == (45, 0)
    assert move_dial(50, "R", 60) == (10, 1)
    assert move_dial(50, "L", 55) == (95, 1)
    assert move_dial(50, "L", 1) == (49, 0)


def move_dial(dial, direction, number):
    if direction == "L":
        # offset = 100-dial
        # if offset == 100:
        #     offset = 0
        # rotations = (offset+number)//100 
        offset = 0 if dial == 0 else (100 - dial)
        rotations = (offset + number) // 100

        return (100+(dial-number))%100, rotations
    elif direction == "R":
        rotations = (dial+number)//100
        return (dial + number) % 100, rotations


with open(INPUT_FILE) as f:
    dial = 50 # starting position
    zero_count = 0

    DEBUG and print("Starting dial:", dial)

    for line in f:
        line = line.rstrip()

        direction = line[0]
        number = int(line[1:])

        dial, cross_zero = move_dial(dial, direction, number)
        DEBUG and print(
            "Rotate", line, "to point at", dial,
            cross_zero and f". During rotation, dial crosses zero {cross_zero} times" or ""
        )

        zero_count += cross_zero
    
        # if dial == 0:
        #     zero_count += 1
        # else:
        #     zero_count += cross_zero


    print("Secret code:", zero_count)

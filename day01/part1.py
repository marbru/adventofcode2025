#!/usr/bin/env python3
# https://adventofcode.com/2025/day/1

DEBUG = True
INPUT_FILE = "./input"

def move_dial(dial, direction, number):
    if direction == "L":
        return (100+(dial-number))%100
    elif direction == "R":
        return (dial + number) % 100


with open(INPUT_FILE) as f:
    dial = 50 # starting position
    zero_count = 0

    DEBUG and print("Starting dial:", dial)

    for line in f:
        line = line.rstrip()

        direction = line[0]
        number = int(line[1:])

        dial = move_dial(dial, direction, number)
        DEBUG and print("Rotate", line, "to point at", dial)

        if dial == 0:
            zero_count += 1


    print("Secret code:", zero_count)

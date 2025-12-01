import sys

sys.stdin = open('day1.input', 'r')
# sys.stdin = open('day1_sample.input', 'r')

def click(start: int, direction: str):
    if direction == 'R':
        if start != 99:
            return start + 1
        else:
            return 0
    elif direction == 'L':
        if start != 0:
            return start - 1
        else:
            return 99
    else:
        raise ValueError

def rotate(start: int, instruction: str):
    direction = instruction[0]
    length = int(instruction[1:])

    counter = 0

    before = start

    for i in range(length):
        after = click(before, direction)

        if after == 0:
            counter += 1
            
        before = after
    
    return after, counter
        

before = 50

master_counter = 0

for i in range(4780):
    after, counter = rotate(before, input())
    
    master_counter += counter
    
    before = after

print(master_counter)
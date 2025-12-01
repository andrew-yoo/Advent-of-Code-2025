import sys

sys.stdin = open('day1.input', 'r')
# sys.stdin = open('day1_sample.input', 'r')

def rotate(start: int, instruction: str):
    direction = instruction[0]

    length = int(instruction[1:])

    if direction == 'R':
        return (start + length) % 100
    elif direction == 'L':
        return (start - length) % 100
    else:
        raise ValueError

before = 50
counter = 0

for i in range(4780):
    after = rotate(before, input())
    
    if after == 0:
        counter += 1
    
    before = after

print(counter)
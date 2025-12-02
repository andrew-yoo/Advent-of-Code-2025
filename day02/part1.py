import sys

sys.stdin = open('input.in', 'r')
# sys.stdin = open('example.in', 'r')

def read():
    return [i for i in input().split(',')]

ranges = read()

invalid = []

for range_ in ranges:
    start, finish = [int(i) for i in range_.split('-')]
    
    for i in range(start, finish + 1):
        
        id_string = str(i)

        length = len(id_string)

        if length % 2 == 0:
            half_length = length // 2

            if id_string[:half_length] == id_string[half_length:]:
                invalid.append(i)


print(sum(invalid))
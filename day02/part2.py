import sys

sys.stdin = open('input.in', 'r')
# sys.stdin = open('example.in', 'r')

def read():
    return [i for i in input().split(',')]

def is_invalid(integer_string: int):

    string = str(integer_string)

    string_length = len(string)

    for repeated_length in range(1, string_length // 2 + 1):
        if string_length % repeated_length == 0:
            if string == string[:repeated_length] * (string_length // repeated_length):
                return True
            
    return False

ranges = read()

invalid = []

for range_ in ranges:
    start, finish = [int(i) for i in range_.split('-')]

    for i in range(start, finish + 1):
        if is_invalid(i):
            invalid.append(i)
        
print(sum(invalid))
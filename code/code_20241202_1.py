import sys

def is_safe(report):
    is_asc = report[0] < report[1]
    for i in range(len(report)-1):
        if (abs(report[i] - report[i+1]) < 1) or (abs(report[i] - report[i+1]) > 3) or ((report[i] < report[i+1]) != is_asc):
            return 0
    return 1

if __name__ == '__main__':
    input_path = './inputs/input_20241202_1.txt'
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    f = open(input_path, "r")
    text = f.read()

    print(sum(map(lambda b: is_safe(list(map(lambda a: int(a), b.split(' ')))), text.split('\n'))))
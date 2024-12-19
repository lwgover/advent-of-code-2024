import sys

def parse_text(text):
    list1 = []
    list2 = []
    for line in text.split('\n'):
        if len(line.split('   ')) < 2:
            continue
        item1, item2 = line.split('   ')
        list1.append(item1)
        list2.append(item2)
    return list1,list2

def distance(list1,list2):
    distance = 0
    # assumes lists are sorted and of the same length
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))
    return distance

def similarity(list1,list2):
    list2_frequencies = {}
    for item in list2:
        if list2_frequencies.get(item) == None:
            list2_frequencies[item] = 1
        else:
            list2_frequencies[item] += 1
    
    similarity_score = 0
    for item in list1:
        similarity_score += int(item) * list2_frequencies[item] if list2_frequencies.get(item) != None else 0

    return similarity_score

if __name__ == '__main__':
    input_path = './inputs/input_20241201_1.txt'
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    f = open(input_path, "r")
    text = f.read()

    list1,list2 = parse_text(text)

    list1.sort()
    list2.sort()

    print(f"Task 1: {distance(list1,list2)}")
    print(f"Task 2: {similarity(list1,list2)}")
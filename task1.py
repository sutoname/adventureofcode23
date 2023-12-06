with open("task1_input.txt") as file:
    indata = file.readlines()


def extractcode(line):
    a = 0
    b = 0
    i = 0
    while not (ord('0') <= ord(line[i]) <= ord('9')):
        i += 1
    a = line[i]
    for i in range(i, len(line)):
        if ord('0') <= ord(line[i]) <= ord('9'):
            b = line[i]
    return int(a+b)


total = 0
for items in indata:
    total += extractcode(items)

print(total)

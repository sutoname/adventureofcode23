with open("task1_input.txt") as file:
    indata = file.readlines()

worddigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


# replace the word digit to numbers

def findworddigit(line):
    newlist = []
    i = 0
    while i <= len(line) - 1:
        # check if its digit - add digit to new list of digits
        if ord('0') <= ord(line[i]) <= ord('9'):
            newlist.append(int(line[i]))
        else:
            for digit in range(9):
                findresult = line.find(worddigits[digit], i)
                if findresult == i:
                    newlist.append(digit + 1)
        i += 1
    # print(line, newlist)
    return newlist[0] * 10 + newlist[-1]


total = 0

for items in indata:
    total += findworddigit(items)

print(total)

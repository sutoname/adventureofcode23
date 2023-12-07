redmax = 12
greenmax = 13
bluemax = 14

with open("day2_input.txt") as file:
    indata = file.readlines()


def setcheck(set):
    if (set['red'] <= redmax) and (set['blue'] <= bluemax) and (set['green'] <= greenmax):
        return True
    else:
        return False


def setparse(set):
    # remove \n at the end of string and then split to list every ball in ine set
    set = set.replace('\n', '').split(', ')
    result = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for ball in set:
        count = int(ball.split(' ')[0])
        colour = ball.split(' ')[1]
        result[colour] = count
    return result


def gamecheck(game):
    game = game.replace('Game ', '')  # remove Game word
    int(game.split(':')[0])
    # sets inside one game in as a List
    game = game.split(': ')[1].split('; ')
    # check every set
    # print(gamenumber, game)
    for set in game:
        # print(setparse(set), setcheck(setparse(set)))
        if not setcheck(setparse(set)):
            return False
    return True


total = 0
index = 1
for item in indata:
    # print(gamecheck(item))
    if gamecheck(item):
        total += index
    index += 1

print(total)

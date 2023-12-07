with open("day2_input.txt") as file:
    indata = file.readlines()


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


def onegamecalc(game):
    game = game.replace('Game ', '')  # remove Game word
    int(game.split(':')[0])
    # sets inside one game in as a List
    game = game.split(': ')[1].split('; ')
    # calc every set
    # print(game)
    currentmaximum = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for set in game:
        # print(setparse(set), setcheck(setparse(set)))
        current_set = setparse(set)
        # print(current_set)
        if currentmaximum['red'] < current_set['red']:
            currentmaximum['red'] = current_set['red']
        if currentmaximum['green'] < current_set['green']:
            currentmaximum['green'] = current_set['green']
        if currentmaximum['blue'] < current_set['blue']:
            currentmaximum['blue'] = current_set['blue']

    return currentmaximum['red'] * currentmaximum['green'] * currentmaximum['blue']


total = 0

for item in indata:
    total += onegamecalc(item)


print(total)

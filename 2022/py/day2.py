with open('../day2.txt') as f:
    # each line is a game. Ex: 'B X'
    games = f.readlines()
    score = 0
    for game in games:
        p1 = game[0]  # player 1 (opponent) move is the first character
        p2 = game[2]  # player 2 (me) move is the third character

        if p1 == 'A':
            if p2 == 'X':
                score += 1 + 3
            elif p2 == 'Y':
                score += 2 + 6
            elif p2 == 'Z':
                score += 3 + 0
        elif p1 == 'B':
            if p2 == 'X':
                score += 1 + 0
            elif p2 == 'Y':
                score += 2 + 3
            elif p2 == 'Z':
                score += 3 + 6
        elif p1 == 'C':
            if p2 == 'X':
                score += 1 + 6
            elif p2 == 'Y':
                score += 2 + 0
            elif p2 == 'Z':
                score += 3 + 3
print(score)


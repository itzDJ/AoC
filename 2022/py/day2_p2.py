with open('../day2.txt') as f:
    # each line is a game. Ex: 'B X'
    games = f.readlines()
    score = 0
    for game in games:
        p1 = game[0]  # player 1 (opponent) move is the first character
        result = game[2]  # the game result is the third character

        if p1 == 'A':
            if result == 'X':
                score += 0 + 3
            elif result == 'Y':
                score += 3 + 1
            elif result == 'Z':
                score += 6 + 2
        elif p1 == 'B':
            if result == 'X':
                score += 0 + 1
            elif result == 'Y':
                score += 3 + 2
            elif result == 'Z':
                score += 6 + 3
        elif p1 == 'C':
            if result == 'X':
                score += 0 + 2
            elif result == 'Y':
                score += 3 + 3
            elif result == 'Z':
                score += 6 + 1
print(score)


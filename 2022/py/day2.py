def part1():
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
    return score

print(f'Part 1: {part1()}')

def part2():
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
    return score

print(f'Part 2: {part2()}')


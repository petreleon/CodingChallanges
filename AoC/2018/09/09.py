from parse import parse

file_opened = open("input_2", 'r')
line = file_opened.read().splitlines()[0]
players, last_mardle = parse("{:d} players; last marble is worth {:d} points", line)

player_scores = [0] * players
row = [0]
current_position = 1
for mardle in range(1, last_mardle+1):
    if mardle % 23 == 0:
        current_position = (current_position - 7) % len(row)
        player_scores[(mardle - 1) % players] = mardle + row[current_position + 1]
        del row[current_position + 1]
    if mardle % 23 != 0:
        current_position = (current_position + 2) % (len(row))
        row.insert(current_position + 1, mardle)

print(max(player_scores))


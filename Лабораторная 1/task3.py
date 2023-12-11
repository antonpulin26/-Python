list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

mid_ind = len(list_players)//2

team1 = list_players[:mid_ind]
team2 = list_players[mid_ind:]

print(team1)
print(team2)

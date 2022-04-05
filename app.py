num_teams = input('\nEnter number of teams: - ')
teams_list = []
for i in range(int(num_teams)):
    teams_list.append(i+1)
if(len(teams_list) % 2) != 0:
    teams_list.append(0)
x = teams_list[0:int(len(teams_list)/2)]
y = teams_list[int(len(teams_list)/2):len(teams_list)]
matches = []
for i in range(len(teams_list)-1):
    rounds = {}
    if i != 0: 
        x.insert(1,y.pop(0))
        y.append(x.pop())
    matches.append(rounds)
    for j in range(len(x)):
            rounds[x[j]] = y[j]
for i in range(len(matches)):
    print('\n Day',i+1, ' : ', matches[i])

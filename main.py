from class_day import Day
import models
from database import init_db, SESSIONLOCAL, ENGINE


class Teams:
    def __init__(self, team):
        self.flag = None
        self.team = team


class Fields:
    def __init__(self, fieldd, dayy: Day):
        self.field = fieldd
        self.day = dayy


class Games:
    def __init__(self, team1, team2, time: str):
        self.team1 = team1
        self.team2 = team2
        self.time = time


init_db()
ENGINE.connect()
database = SESSIONLOCAL()

pr = database.query(models.Team).all()

mass_teams = []

for i in range(len(pr)):
    c = Teams(pr[i])
    mass_teams.append(c)
    if pr[i].time_wish is not None:
        mass_teams[i].flag = True

days_db = database.query(models.Field).all()

days = []

for i in range(len(days_db)):
    k = days_db[i]
    day = Day(days_db[i].start_time, days_db[i].duration)
    field = Fields(k, day)
    days.append(field)

mass_games = []

stadiums = []

for i in range(len(days_db)):
    stadiums.append(days_db[i].stadium)

stadiums = list(set(stadiums))

for i in range(len(stadiums)):
    f = stadiums[i]
    '''# массив, в котором хранятся команды с пожеланием по определенному стадиону
    s = database.query(models.Team).filter(models.Team.stadium_wish == f).all()'''
    s = []
    for j in range(len(mass_teams)):
        if mass_teams[j].team.stadium_wish == f:
            s.append(mass_teams[j])
    '''print(f)
    print(":")
    for k in range(len(s)):
        print(s[k].team.name)'''

    use_fields = []  # массив days, отсортированный по стадиону
    for k in range(len(days)):
        if days[k].field.stadium == f:
            use_fields.append(days[k])
    '''print(use_fields[0].field.start_time, use_fields[0].field.duration)
    print(s[0].team.time_wish)
    for p in range(len(s)):
        print(s[p].team.name)
        print(s[p].team.time_wish)'''
    while len(s) > 1:
        for q in range(len(s) - 1):
            if len(s) < 1:
                break
            n_left = int(s[0].team.time_wish[:2])
            n_right = int(s[0].team.time_wish[6:-3])
            m_left = int(s[q + 1].team.time_wish[:2])
            m_right = int(s[q + 1].team.time_wish[6:-3])
            if m_left <= n_left <= m_right or m_left <= n_right <= m_right or n_left <= m_right <= n_right or n_left <= m_left <= n_right:
                if m_left <= n_left <= m_right: # skoree vsego nuzhno budet dobavit eshe odno uslovie o granicah s dregih storon
                    for count in range(len(use_fields)):
                        for durat in range(len(use_fields[count].day.mass_time) - 1):
                            if n_left <= use_fields[count].day.mass_time[durat] <= m_right and use_fields[count].day.mass_time[durat+1] - use_fields[count].day.mass_time[durat] == 1.5\
                                    and len(s) > q:
                                k = Games(s[0], s[q + 1], str(use_fields[count].day.mass_time[durat]))
                                mass_games.append(k)
                                print(s[0].team.name, s[q + 1].team.name, use_fields[count].day.mass_time[durat])
                                s.pop(0)
                                s.pop(q)
                                '''
                                print("\n")
                                for inn in range(len(s)):
                                    print(s[inn].team.name)
                                print("\n")
                                '''
                                use_fields[count].day.mass_time.pop(durat)
                elif m_left <= n_right <= m_right: # skoree vsego nuzhno budet dobavit eshe odno uslovie o granicah s dregih storon
                    for count in range(len(use_fields)):
                        for durat in range(len(use_fields[count].day.mass_time) - 1):
                            if n_right <= use_fields[count].day.mass_time[durat] <= m_right and use_fields[count].day.mass_time[durat+1] - use_fields[count].day.mass_time[durat] == 1.5\
                                    and len(s) > q:
                                k = Games(s[0], s[q+1], str(use_fields[count].day.mass_time[durat]))
                                mass_games.append(k)
                                print(s[0].team.name, s[q + 1].team.name, use_fields[count].day.mass_time[durat])
                                s.pop(0)
                                s.pop(q)
                                '''
                                print("\n")
                                for inn in range(len(s)):
                                    print(s[inn].team.name)
                                print("\n")
                                '''
                                use_fields[count].day.mass_time.pop(durat)
                elif n_left <= m_right <= n_right: # skoree vsego nuzhno budet dobavit eshe odno uslovie o granicah s dregih storon
                    for count in range(len(use_fields)):
                        for durat in range(len(use_fields[count].day.mass_time) - 1):
                            if m_right <= use_fields[count].day.mass_time[durat] <= n_right and use_fields[count].day.mass_time[durat+1] - use_fields[count].day.mass_time[durat] == 1.5\
                                    and len(s) > q:
                                k = Games(s[0], s[q+1], str(use_fields[count].day.mass_time[durat]))
                                mass_games.append(k)
                                print(s[0].team.name, s[q + 1].team.name, use_fields[count].day.mass_time[durat])
                                s.pop(0)
                                s.pop(q)
                                '''
                                print("\n")
                                for inn in range(len(s)):
                                    print(s[inn].team.name)
                                print("\n")
                                '''
                                use_fields[count].day.mass_time.pop(durat)
                elif n_left <= m_left <= n_right: # skoree vsego nuzhno budet dobavit eshe odno uslovie o granicah s dregih storon
                    for count in range(len(use_fields)):
                        for durat in range(len(use_fields[count].day.mass_time) - 1):
                            if m_left <= use_fields[count].day.mass_time[durat] <= n_right and use_fields[count].day.mass_time[durat+1] - use_fields[count].day.mass_time[durat] == 1.5\
                                    and len(s) > q:
                                k = Games(s[0], s[q+1], str(use_fields[count].day.mass_time[durat]))
                                mass_games.append(k)
                                print(s[0].team.name, s[q + 1].team.name, use_fields[count].day.mass_time[durat])
                                s.pop(0)
                                s.pop(q)
                                '''
                                print("\n")
                                for inn in range(len(s)):
                                    print(s[inn].team.name)
                                print("\n")
                                '''
                                use_fields[count].day.mass_time.pop(durat)
        break



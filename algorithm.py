from math import floor
from sqlalchemy import select
from class_day import Day
import models
from database import init_db, SESSIONLOCAL, ENGINE
from XLSX_handler import load_to_file


class Teams:
    def __init__(self, team):
        self.flag = None
        self.team = team


class Fields:
    def __init__(self, fieldd, dayy: Day):
        self.field = fieldd
        self.day = dayy


class Games:
    def __init__(self, team1, team2, time: str, field, stadium):
        self.team1 = team1
        self.team2 = team2
        self.time = time
        self.field = field
        self.stadium = stadium


def calculate(database, path):
    divisions = []

    prr = database.query(models.Team).all()
    days_db = database.query(models.Field).all()

    for i in range(len(prr)):
        divisions.append(prr[i].division)

    divisions = list(set(divisions))

    for division in divisions:
        pr = database.query(models.Team).filter(models.Team.division == division).all()
        mass_teams = []
        for i in range(len(pr)):
            c = Teams(pr[i])
            mass_teams.append(c)
            if pr[i].time_wish is not None:
                mass_teams[i].flag = True

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
            # массив, в котором хранятся команды с пожеланием по определенному стадиону
            s = []
            for j in range(len(mass_teams)):
                if mass_teams[j].team.stadium_wish == f:
                    s.append(mass_teams[j])
            use_fields = []  # массив days, отсортированный по стадиону
            for k in range(len(days)):
                if days[k].field.stadium == f:
                    use_fields.append(days[k])

            while len(s) > 1:
                q = 0
                while q < len(s) - 1:
                    if len(s) < 2:
                        break
                    try:
                        while s[q].team.format != s[0].team.format and s[0].team.coach == s[q].team.coach:
                            q += 1
                    except:
                        print("Невозможно составить расписание")
                        return -1

                    left = int(max(s[0].team.time_wish[:2], s[q + 1].team.time_wish[:2]))
                    right = int(min(s[0].team.time_wish[6:-3], s[q + 1].team.time_wish[6:-3]))
                    if left <= right:
                        size = len(mass_games)
                        for count in range(len(use_fields)):
                            if len(mass_games) > size:
                                break
                            durat = 0
                            while len(use_fields[count].day.mass_time) > durat + 1:

                                if left <= use_fields[count].day.mass_time[durat] <= right and (
                                        use_fields[count].day.mass_time[durat] == use_fields[count].day.mass_time[-1] or \
                                        use_fields[count].day.mass_time[durat + 1] - use_fields[count].day.mass_time[
                                            durat] == int(use_fields[count].day.duration) / 60) \
                                        and len(s) > 1:
                                    '''print(s[0].team.name, s[q + 1].team.name,
                                          str(use_fields[count].day.mass_time[durat]),
                                          use_fields[count].field.name)'''
                                    k = Games(s[0], s[q + 1], str(use_fields[count].day.mass_time[durat]),
                                              use_fields[count].field.name, s[0].team.stadium_wish)
                                    mass_games.append(k)
                                    s[0].team.count_of_matches += 1
                                    s[q + 1].team.count_of_matches += 1
                                    #print(s[0].team.count_of_matches)
                                    if s[0].team.count_of_matches == 2:
                                        s.pop(0)

                                    else:
                                        q += 1
                                    if s[q].team.count_of_matches == 2:
                                        s.pop(q)
                                    use_fields[count].day.mass_time.pop(durat)
                                    break
                                else:
                                    durat += 1

                    else:
                        print("Нельзя составить")
                        return -2
                q += 1
        out_teams = []

        for count in range(len(pr)):
            counting = 0
            for i in range(len(mass_games)):
                if mass_teams[count].flag and mass_teams[count].team.name == mass_games[i].team1.team.name or \
                        mass_teams[count].team.name == mass_games[i].team2.team.name:
                    counting += 1
            if counting == 0:
                out_teams.append(mass_teams[count].team)

        tmp = []
        for i in mass_games:
            # print(i.team1.team.name, i.team2.team.name, i.time)
            tmp.append((push_to_db(i, database)))
        print(tmp)
        load_to_file(database, path, games=tmp)
        return 0

    # TODO нужно составить матчи с командами из out_teams и mass_teams, у к-ых !=flag
    # TODO нужно составить матчи для всех командов, к-ые остались в mass_teams, у к-ых !=flag
    # TODO возможно(если он заметит) нужно будет составить вторые матчи для каждый команды (просто q в s увеличить на 1 по модулю len(s))
    # TODO связать название поля и команды для вывода (или забить хуй)


def normalize_time(s):
    try:
        mins = str(int((float(s) - floor(float(s))) * 60))
        if len(mins) != 2:
            mins += '0'
        i = str(floor(float(s))) + ":" + mins
        return i
    except:
        return s


def push_to_db(game: Games, database):
    stmt_div = select(models.Team.division).where(models.Team.name == game.team1.team.name)
    div = database.execute(stmt_div).all()[0][0]
    stmt_stadium = select(models.Field.stadium).where(models.Field.name == game.field)
    stadium = database.execute(stmt_stadium).all()[0][0]
    # print("stadium:", stadium)
    # print("division", div)
    '''print(
        game.team1.team.name,
        game.team2.team.name,
        normalize_time(game.time),
        stadium,
        game.field,
        div)
    try:
        new_game = models.Games(team1=game.team1.team.name,
                                team2=game.team2.team.name,
                                start_time=normalize_time(game.time),
                                stadium=stadium,
                                field=game.field,
                                division=div)
        database.add(new_game)
        database.commit()
    except:
        pass'''
    return [game.team1.team.name,
            game.team2.team.name,
            normalize_time(game.time),
            stadium,
            game.field,
            div]




if __name__ == "__main__":
    init_db()
    ENGINE.connect()
    database = SESSIONLOCAL()
    file = "C:\\Users\\Danil\\Desktop\\tmp\\расписание.xlsx"
    calculate(database, file)

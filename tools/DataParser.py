class DataParser:
    @staticmethod
    def form_divs(dump1):
        divs = sorted(set([i[1] for i in dump1]))
        res = {i: [] for i in divs}
        for i in dump1:
            for j in divs:
                if i[1] == j:
                    res[j].append(i[0])

        return res


if __name__ == "__main__":
    a = [
        ['пидоры', '1-й дивизион', '5', 'Хуев Г.М.', '05.04.2020', '1', '12:00-20:00', '00:00-24:00'],
        ['гниды', '2-й дивизион', '5', 'Хуев Г.М.', '05.04.2020', '1', '12:00-20:00', '06:00-12:00'],
        ['гр. 7333', '2-й дивизион', '5', 'Хуев Г.М.', '05.04.2020', '1', '12:00-20:00', '00:00-24:00'],
        ['мертвые шлюхи', '2-й дивизион', '5', 'Анилингус Е.А.', '05.04.2020', '1', '12:00-20:00', '00:00-24:00'],
        ['дети блядей', '2-й дивизион', '7', 'Хуев Г.М.', '05.04.2020', '1', '06:00-12:00', '00:00-24:00'],
        ['норм типы', '1-й дивизион', '3', 'Анилингус Е.А.', '05.04.2020', '1', '12:00-20:00', '00:00-24:00'],
        ['вонючие хуесосы', '3-й дивизион', '3', 'Хуев Г.М.', '05.04.2020', '1', '12:00-20:00', '00:00-24:00'],
        ['гандоны', '3-й дивизион', '7', 'Хуев Г.М.', '05.04.2020', '2', '12:00-20:00', '06:00-12:00'],
        ['редкостные ебни', '1-й дивизион', '3', 'Анилингус Е.А.', '05.04.2020', '2', '06:00-12:00', '00:00-24:00'],
        ['днище', '1-й дивизион', '3', 'Анилингус Е.А.', '05.04.2020', '1', '06:00-12:00', '00:00-24:00']
    ]
    dp = DataParser()
    dp.form_divs(a)

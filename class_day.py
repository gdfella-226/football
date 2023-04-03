class Day:
    def __init__(self, start_time: str, duration):
        self.mass_time = []
        start = round(float(start_time[-2:]) / 60, 2)
        i = 0
        while start + float(duration) * i < 24:
            self.mass_time.append(i)
            i += 1

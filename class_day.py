class Day:
    def __init__(self, start_time: str, duration):
        self.duration = duration
        self.start_time = start_time
        self.mass_time = []
        duration = float(duration)/60
        start = float(start_time[-2:]) / 60 + float(start_time[:-3])
        i = 0
        while start + float(duration) * i < 24:
            self.mass_time.append(start + duration * i)
            i += 1

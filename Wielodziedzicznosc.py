# Zadanie wielodziedziczność

class movie:
    def __init__(self, title, year, type, views)
        self.title = title
        self.year = year
        self.type = type
        self.views = views

class series(movie):
    def __init__(self, episode_number, season_number)
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

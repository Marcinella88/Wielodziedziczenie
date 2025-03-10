# Zadanie wielodziedziczność

class Movie:
    def __init__(self, title, year, type_movie, views):
        self.title = title
        self.year = year
        self.type_movie = type_movie
        self.views = views
    
    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.year})"    
       
class Series(Movie):
    def __init__(self, episode_number, season_number,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.episode_number}E{self.season_number}"


movie_1 = Movie(title="The Green Mile", year="1999", type_movie="drama", views=0)
movie_2 = Movie(title="The Shawshank Redemption", year="1994", type_movie="drama", views=0)
movie_3 = Movie(title="Forrest Gump", year="1994", type_movie="comedy", views=0)
movie_4 = Movie(title="Leon", year="1994", type_movie="drama", views=0)
movie_5 = Movie(title="The Matrix", year="1999", type_movie="Sci-Fi", views=0)

series_1 = Series(title="Game of trones", year="2011", type_movie="drama", views=0, episode_number=1, season_number=1)
series_2 = Series(title="Game of trones", year="2011", type_movie="drama", views=0, episode_number=2, season_number=1)
series_3 = Series(title="Game of trones", year="2011", type_movie="drama", views=0, episode_number=3, season_number=1)
series_4 = Series(title="Game of trones", year="2011", type_movie="drama", views=0, episode_number=1, season_number=2)
series_5 = Series(title="Game of trones", year="2011", type_movie="drama", views=0, episode_number=2, season_number=2)
series_6 = Series(title="Game of trones", year="2011", type_movie="drama", views=0, episode_number=3, season_number=2)
series_7 = Series(title="Breaking Bad", year="2008", type_movie="drama", views=0, episode_number=1, season_number=1)
series_8 = Series(title="Breaking Bad", year="2008", type_movie="drama", views=0, episode_number=2, season_number=1)
series_9 = Series(title="Breaking Bad", year="2008", type_movie="drama", views=0, episode_number=1, season_number=2)
series_10 = Series(title="Breaking Bad", year="2008", type_movie="drama", views=0, episode_number=2, season_number=2)
import random
from datetime import datetime

class Movie:
    all_objects = []
    
    def __init__(self, title, year, type_movie, views):
        self.title = title
        self.year = year
        self.type_movie = type_movie
        self.views = views
        Movie.all_objects.append(self)

    def __str__(self):
        return f'"{self.title}" ({self.year})'
    
    def play(self):
        self.views += 1

    def get_movies(all_objects):
        return sorted([obj for obj in all_objects if obj.__class__.__name__ == "Movie"], key=lambda obj: obj.title)
    
    def get_series(all_objects):
        return sorted([obj for obj in all_objects if obj.__class__.__name__ == "Series"], key=lambda obj: obj.title)
              
    def search(title):
        result_searching = [obj for obj in all_objects if title == obj.title]
        if len(result_searching) == 0:
            print("Brak wyszukań!")
        return result_searching

    def generate_views(all_objects):
        random_movies = random.choice(all_objects)
        random_movies.views += random.randint(1,100)
        return random_movies

    def add_views(all_objects):
        for e in range(10):
            Movie.generate_views(all_objects)

    def top_titles(all_objects, ilosc):
        _sorted_list = sorted(all_objects, key= lambda x: x.views, reverse=True)
        sorted_list = _sorted_list[:ilosc]
        return sorted_list
    
  
class Series(Movie):
    def __init__(self, episode_number, season_number,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'"{self.title}" S{(str(self.season_number)).zfill(2)}E{(str(self.episode_number)).zfill(2) }'
    

if __name__ == "__main__":

    movie_1 = Movie(title="The Green Mile", year="1999", type_movie="drama", views=0)
    movie_2 = Movie(title="The Shawshank Redemption", year="1994", type_movie="drama", views=0)
    movie_3 = Movie(title="Forrest Gump", year="1994", type_movie="comedy", views=0)
    movie_4 = Movie(title="Leon", year="1994", type_movie="drama", views=0)
    movie_5 = Movie(title="The Matrix", year="1999", type_movie="Sci-Fi", views=0)
    
    series_1 = Series(title="Game of Trones", year="2011", type_movie="drama", views=0, episode_number=1, season_number=1)
    series_2 = Series(title="Game of Trones", year="2011", type_movie="drama", views=0, episode_number=2, season_number=1)
    series_3 = Series(title="Game of Trones", year="2011", type_movie="drama", views=0, episode_number=3, season_number=1)
    series_4 = Series(title="Game of Trones", year="2011", type_movie="drama", views=0, episode_number=1, season_number=2)
    series_5 = Series(title="Game of Trones", year="2011", type_movie="drama", views=0, episode_number=2, season_number=2)
    series_6 = Series(title="Game of Trones", year="2011", type_movie="drama", views=0, episode_number=3, season_number=2)
    series_7 = Series(title="Breaking Bad", year="2008", type_movie="drama", views=0, episode_number=1, season_number=1)
    series_8 = Series(title="Breaking Bad", year="2008", type_movie="drama", views=0, episode_number=2, season_number=1)
    series_9 = Series(title="Breaking Bad", year="2008", type_movie="drama", views=0, episode_number=1, season_number=2)
    series_10 = Series(title="Breaking Bad", year="2008", type_movie="drama", views=0, episode_number=2, season_number=2)

    all_objects = Movie.all_objects
    dzis = datetime.now()
    date_now = dzis.strftime("%d.%m.%Y")
 
    print(f"Biblioteka filmów:")
    for e in all_objects:
        print(f"{e}")
        
    Movie.add_views(all_objects)

    print(f"Najpopularniejsze filmy i seriale z dnia {date_now}:")
    for e in Movie.top_titles(all_objects, 3):
        print(e)
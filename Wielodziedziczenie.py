import random
from datetime import datetime

class Movies:
    def __init__(self, title, year, type_movie, views):
        self.title = title
        self.year = year
        self.type_movie = type_movie
        self.views = views

    def __str__(self):
        return f'"{self.title}" ({self.year})'
    
    def play(self):
        self.views += 1

class Series(Movies):
    def __init__(self, episode_number, season_number,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
 
    def __str__(self):
        return f'"{self.title}" S{(str(self.season_number)).zfill(2)}E{(str(self.episode_number)).zfill(2)}'


def generate_date_now():
    return datetime.now().strftime("%d.%m.%Y")

def get_elements(catalog, type_to_filter):
    return sorted([ e for e in catalog if type(e) == type_to_filter], key=lambda item: item.title)

def get_movies(catalog):
    return get_elements(catalog, Movies)
 
def get_series(catalog):
    return get_elements(catalog, Series)

def search(catalog, title):
    result_searching = [i for i in catalog if title == i.title]
    if len(result_searching) == 0:
        print("Brak wyszukań!")
    return result_searching
 
def generate_views(catalog):
    random_movies = random.choice(catalog)
    random_movies.views += random.randint(1,100)
    return random_movies
 
def add_views(catalog, number_of_performances):
    for _ in range(number_of_performances):
        generate_views(catalog)
 
def top_titles(catalog, quantity_top_titles):
    _sorted_list = sorted(catalog, key= lambda item: item.views, reverse=True)
    sorted_list = _sorted_list[:quantity_top_titles]
    return sorted_list

if __name__ == "__main__":

    movie_1 = Movies(title="The Green Mile", year="1999", type_movie="drama", views=0)
    movie_2 = Movies(title="The Shawshank Redemption", year="1994", type_movie="drama", views=0)
    movie_3 = Movies(title="Forrest Gump", year="1994", type_movie="comedy", views=0)
    movie_4 = Movies(title="Leon", year="1994", type_movie="drama", views=0)
    movie_5 = Movies(title="The Matrix", year="1999", type_movie="Sci-Fi", views=0)
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
 
    all_movies = [movie_1, movie_2, movie_3, movie_4, movie_5]
    all_series = [series_1, series_2, series_3, series_4, series_5, series_6, series_7, series_8, series_9, series_10]
    catalog = all_movies + all_series
    
    print(f"Biblioteka filmów:")
    for e in catalog:
        print(f"{e}")
 
    add_views(catalog, 10)

    print(f"Najpopularniejsze filmy i seriale z dnia {generate_date_now()}:")
    for e in top_titles(catalog, 3):
        print(e)
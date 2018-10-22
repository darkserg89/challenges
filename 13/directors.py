import csv
from collections import defaultdict, namedtuple, Counter
from pprint import pprint

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    Movie = namedtuple('Movie','title, year, score')
    with open('movie_metadata.csv') as f:
        reader = csv.DictReader(f)
        for line in reader:
            try:
                director = line['director_name']
                movie = line['movie_title'].strip('\xa0')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title = movie, year = year, score = score)
            directors[director].append(m)
    return directors
        

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    pass


def _calc_mean(directors):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    cnt = Counter()
    for director, movies in directors.items():
        if len(movies) >= 4 :
            cnt[director] += len(movies)
    return cnt


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
#    main()
    directors = get_movies_by_director()
    pprint(len(directors['Christopher Nolan']))
    cnt = _calc_mean(directors)
    pprint(cnt['Christopher Nolan'])
    pprint(cnt)

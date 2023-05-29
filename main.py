from PyMovieDb import IMDB
imdb = IMDB()

def Movie_by_name():
    name_search = input('Enter Title >:')
    res = imdb.get_by_name(f'{name_search}')
    print(res)
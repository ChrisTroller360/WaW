from PyMovieDb import IMDB
imdb = IMDB()
    
if __name__ == '__main__':
    name_search = input('Enter Title >:')
    res = imdb.get_by_name(f'{name_search}')
    print(res) 
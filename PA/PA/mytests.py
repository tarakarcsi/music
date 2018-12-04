listoflists = [
            ["Pink Floyd", "The Dark Side Of The Moon", "1973", "progressive rock", "43:00"],
            ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
            ["The Beatles", "Revolver", "1966", "rock", "34:43"],
            ["Deep Purple", "Machine Head", "1972", "hard rock", "37:25"],
            ["Old Timers", "Old Time", "966", "ancient", "123:45"],
            ["Pink Floyd", "Wish You Were Here", "1975", "progressive rock", "44:28"],
            ["Boston", "Boston", "1976", "hard rock", "37:41"],
            ["Monika Brodka", "Granada", "2010", "pop", "37:42"],
            ["David Bowie", "Low", "1977", "rock", "38:26"],
            ["rock", "rock", "966", "pop", "13:37"],
            ["Massive Attack", "Blue Lines", "1991", "hip hop", "45:02"]]

def get_longest_album(albums):
    longest_album = 0
    for line in range(len(albums)):
        if albums[line][3] > longest_album:
            longest_album = albums[line][3]
    
    for line in range(len(albums)):
        if longest_album in albums[line]:
            return albums[line]



def get_genre_stats(albums):
    genre_dict = {}
    genre_list = []
    for line in range(len(albums)):
        genre_list.append(albums[line][3])

    for element in genre_list:
        if element in genre_dict:
            genre_dict[element] += 1
        else:
            genre_dict[element] = 1

    return genre_dict

def get_last_oldest(albums):
    oldest_years_list = []
    oldests_year = int(albums[0][2])
    for line in range(len(albums)):
        if int(albums[line][2]) < oldests_year:
            oldests_year = albums[line][2]
    
    for line in range(len(albums)):
        if oldests_year in albums[line]:
            oldest_years_list.append(albums[line])
    return oldest_years_list[-1]

def get_last_oldest_of_genre(albums, genre):

    list_of_given_genres = []
    for line in range(len(albums)):
        if genre in albums[line]:
            list_of_given_genres.append(albums[line])
    return get_last_oldest(list_of_given_genres))


def get_longest_album(albums):
    timestamps = []
    for line in range(len(albums)):
        converted_to_float = float(albums[line][4].replace(':', '.'))
        timestamps.append(converted_to_float)
    longest_one = str(max(timestamps)).replace('.', ':')

    for line in range(len(albums)):
        if longest_one in albums[line]:
            return albums[line]

def get_albums_by_genre(albums, genre):
    list_of_albums_by_genre = []
    for line in albums:
        if line[3] == genre:
            list_of_albums_by_genre.append(line)
    return list_of_albums_by_genre 


def get_total_albums_length(albums):
    minutes = []
    seconds = []
    lengths = []
    for line in range(len(albums)):
        lengths.append(albums[line][4].split(':'))
    for i in lengths:
        minutes.append(int(i[0])*60)
        seconds.append(int(i[1]))
    total_lenght_in_seconds = sum(minutes) + sum(seconds)
    return total_lenght_in_seconds/60


    
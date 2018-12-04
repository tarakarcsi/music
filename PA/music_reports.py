def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    list_of_albums_by_genre = []
    for line in albums:
        if line[3] == genre:
            list_of_albums_by_genre.append(line)
    return list_of_albums_by_genre 


def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
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

def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    timestamps = []
    for line in range(len(albums)):
        converted_to_float = float(albums[line][4].replace(':', '.'))
        timestamps.append(converted_to_float)
    longest_one = str(max(timestamps)).replace('.', ':')

    for line in range(len(albums)):
        if longest_one in albums[line]:
            return albums[line]


def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    oldest_years_list = []
    oldests_year = int(albums[0][2])
    for line in range(len(albums)):
        if int(albums[line][2]) < int(oldests_year):
            oldests_year = albums[line][2]
    
    for line in range(len(albums)):
        if oldests_year in albums[line]:
            oldest_years_list.append(albums[line])

    return oldest_years_list[-1]
    



def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """
    
    list_of_given_genres = []
    for line in range(len(albums)):
        if genre in albums[line]:
            list_of_given_genres.append(albums[line])
    return get_last_oldest(list_of_given_genres)
    

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
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
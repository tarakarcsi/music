"""
The main program should use functions from music_reports and display modules
"""
import music_reports
import display
import file_handling

def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """

def choose_option():
    chosen_option = input('Please choose an option from: ')

    if chosen_option == '0':
        input_genre = input('Please enter a genre:')
        display.print_albums_list(music_reports.get_albums_by_genre(file_handling.import_data(filename = 'albums_data.txt'),input_genre))
    elif chosen_option == '1':
        print(music_reports.get_genre_stats(file_handling.import_data(filename = 'albums_data.txt')))
    elif chosen_option == '2':
        display.print_album_info(music_reports.get_last_oldest(file_handling.import_data(filename = 'albums_data.txt')))
    elif chosen_option == '3':
        input_genre_again = input('Please enter a genre:')
        display.print_album_info(music_reports.get_last_oldest_of_genre(file_handling.import_data(filename = 'albums_data.txt'), input_genre_again))
    elif chosen_option == '4':
        display.print_album_info(music_reports.get_longest_album(file_handling.import_data(filename = 'albums_data.txt')))
    elif chosen_option == '5':
        print('{} minutes'.format(music_reports.get_total_albums_length(file_handling.import_data(filename = 'albums_data.txt'))))
    
def menu_commands():
    options = ["Get albums by genre",
               "Get genre stats",
               "Get last oldest album",
               "Get last oldest album by genre",
               "Get the longest album",
               "The lenght of all albums"]
    return options

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    while True:
        display.print_program_menu(menu_commands())
        choose_option()



if __name__ == '__main__':
    main()

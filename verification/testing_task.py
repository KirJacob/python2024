def flatten(*args):
    result = []
    for element in args:
        result = result + element
    return result


# flatten([[1, 2], [3, 4]]) ==> [1, 2, 3, 4]
# print(flatten([1, 2], [3, 4]))


# Write the function that should receive few numbers as arguments
# and return a sorted string with unused digits.
# Examples: unused_digits(12, 34, 56, 78) == "09"

def unused_digits(*args):
    rng_num = set(range(10))
    digits_list = []
    for num in args:
        digits_list = digits_list + list(str(num))
    digits_list_num = list(map(lambda x: int(x), digits_list))
    digits_list_num.sort()
    set_num = set(digits_list_num)
    result_num = rng_num.difference(set_num)
    result_num_str = list(map(lambda x: str(x), result_num))
    return "".join(result_num_str)


# print(unused_digits(12, 34, 56, 78))


# Create get_song(db, len_seconds) helper function that takes two parameters -
# list with dictionary with songs (see below) and integer argument which is a maximum length
# of a song in seconds.
# songs is an array of objects which are formatted as follows:

# Result should be a title of the longest song from the database that matches
# the criteria of not being longer than specified time.

# If there's no songs matching criteria in the database, return False. print(get_song(songs_db, 145))

songs_db = [{
    'artist': 'Led Zeppelin',
    'title': 'Stairways to heaven',
    'playback': '09:20'
}, {
    'artist': 'Metallica',
    'title': 'Master of puppets',
    'playback': '04:30'
}, {
    'artist': 'Nirvana',
    'title': 'The Man who sold the world',
    'playback': '03:10'
}, {
    'artist': 'Stepan',
    'title': 'Letter to mom',
    'playback': '02:20'
}]


class Song:

    def __init__(self, artist, title, playback):
        self.artist = artist
        self.title = title
        self.playback = playback

    def __str__(self):
        return f"[{self.artist}, {self.title}, {self.playback}, {self.get_playback_sec()}]"

    def get_playback_sec(self):
        playback_lst = str(self.playback).split(":")
        return int(playback_lst[0]) * 60 + int(playback_lst[1])


def get_song(db, len_seconds):
    songs_objs = list(map(lambda song: Song(song["artist"], song["title"], song["playback"]), db))
    song_objs_filtered = list(filter(lambda song: song.get_playback_sec() <= len_seconds, songs_objs))
    song_title_playback = list(map(lambda song: int(song.get_playback_sec()), song_objs_filtered))
    if len(song_title_playback) > 0:
        max_playback = max(song_title_playback)
        res_song = list(filter(lambda song: song.get_playback_sec() == max_playback, song_objs_filtered))
    else:
        return False
    return res_song[0].title


print(get_song(songs_db, 190))# should return Master of puppets

# Table1
# OrderID
# CustomerID
# SalaryDate
#
# Table 2
#
#
# CustomerID
# CustomerName
# Salary
# Country
#
# Show CustomerName, SalaryDate, Country, where Salary > 1000


select t2.CustomerName, t1.SalaryDate, t2.Country from table1 as t1
right join table2 as t2 on t1.CustomerID = t2.CustomerID
where t2.Salary > 1000

select avg(Salary)
from table2
group by 


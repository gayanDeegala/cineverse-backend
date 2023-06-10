from enum import Enum
from collections import namedtuple


class Date(Enum):
    today = 'Today'
    June10 = 'Sat, 10 June'
    June11 = 'Sun, 11 June'
    June12 = 'Mon, 12 June'
    June13 = 'Tue, 13 June'
    June14 = 'Wed, 14 June'
    June15 = 'Thu, 15 June'


class ShowTime(Enum):
    AM10 = '10:00 AM'
    PM1 = '1:00 PM'
    PM4 = '4:00 PM'
    PM7 = '7:00 PM'


class Theatre(Enum):
    THEATRE_1 = 'Theatre 1', {
        'A': 18,
        'B': 20,
        'C': 20,
        'D': 20,
        'E': 20,
        'F': 20,
        'G': 20,
        'H': 20,
        'I': 20,
        'J': 20,
        'K': 18,
        'L': 18,
        'M': 9
    }
    THEATRE_2 = 'Theatre 2', {
        'A': 15,
        'B': 17,
        'C': 18,
        'D': 19,
        'E': 19,
        'F': 21,
        'G': 21,
        'H': 20
    }
    THEATRE_3 = 'Theatre 3', {
        'A': 7,
        'B': 8,
        'C': 9,
        'D': 8,
        'E': 9,
        'F': 8,
        'G': 6,
        'H': 4
    }


class MovieTitle(Enum):
    SpiderManAcrossTheSpiderVerse = 'Spider-Man: Across the Spider-Verse'
    GuardiansOfTheGalaxyVol3 = 'Guardians of the Galaxy Vol. 3'
    FastX = 'Fast X'
    TheLittleMermaid = 'The Little Mermaid'


class Event:
    def __init__(self, date, show_time, theatre, movie_title):
        self.date = date
        self.show_time = show_time
        self.theatre = theatre
        self.movie_title = movie_title


BookedSeats = namedtuple('BookedSeats', ['seats'])

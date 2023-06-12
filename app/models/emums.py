from enum import Enum

from app.database.data.seating import THEATRE_1_SEATING, THEATRE_2_SEATING, THEATRE_3_SEATING


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
    THEATRE_1 = 'Theatre 1'
    THEATRE_2 = 'Theatre 2'
    THEATRE_3 = 'Theatre 3'

    def get_seating_arrangement(self):
        if self == Theatre.THEATRE_1:
            return THEATRE_1_SEATING
        elif self == Theatre.THEATRE_2:
            return THEATRE_2_SEATING
        elif self == Theatre.THEATRE_3:
            return THEATRE_3_SEATING


class MovieTitle(Enum):
    SpiderManAcrossTheSpiderVerse = 'Spider-Man: Across the Spider-Verse'
    GuardiansOfTheGalaxyVol3 = 'Guardians of the Galaxy Vol. 3'
    FastX = 'Fast X'
    TheLittleMermaid = 'The Little Mermaid'

from typing import List
from app.models.emums import MovieTitle, Date, ShowTime, Theatre
import json

movieTitles: List[MovieTitle] = [
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.SpiderManAcrossTheSpiderVerse,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.GuardiansOfTheGalaxyVol3,
    MovieTitle.FastX,
    MovieTitle.FastX,
    MovieTitle.FastX,
    MovieTitle.TheLittleMermaid,
    MovieTitle.TheLittleMermaid,
    MovieTitle.TheLittleMermaid,
]

dummy_bookings = ['C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'G10', 'G11', 'J5',
                  'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13']

events_data = []
i = 0
for date in Date:
    for showTime in ShowTime:
        for theatre in Theatre:
            theater_name = Theatre(theatre).value
            if theatre == Theatre.THEATRE_1:
                event = (
                    date.value,
                    showTime.value,
                    theater_name,
                    movieTitles[i % len(movieTitles)].value,
                    json.dumps(dummy_bookings),
                )
            else:
                event = (
                    date.value,
                    showTime.value,
                    theater_name,
                    movieTitles[i % len(movieTitles)].value,
                    json.dumps([]),
                )
            events_data.append(event)
            i += 1

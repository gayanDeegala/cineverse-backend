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

events_data = []
i = 0
for date in Date:
    for showTime in ShowTime:
        for theatre in Theatre:
            theater_name = Theatre(theatre).value[0]
            event = (
                date.value,
                showTime.value,
                theater_name,
                movieTitles[i % len(movieTitles)].value,
                json.dumps(['A1', 'A2']),
            )
            events_data.append(event)
            i += 1

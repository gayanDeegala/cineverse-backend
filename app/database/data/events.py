from typing import List
from app.models.types import MovieTitle, Date, ShowTime, Theatre


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
                '[]',
            )
            events_data.append(event)
            i += 1

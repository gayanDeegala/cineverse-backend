from pydantic import BaseModel
from collections import namedtuple


class Event(BaseModel):
    id: int
    date: str
    show_time: str
    theatre: str
    movie_title: str
    booked_seats: str


BookedSeats = namedtuple('BookedSeats', ['seats'])

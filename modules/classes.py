from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(eq=True)
class Presence:
    userId: int
    userPresenceType: int
    lastLocation: str
    placeId: Optional[int]
    rootPlaceId: Optional[int]
    gameId: Optional[int]
    universeId: Optional[int]
    userPresenceTypeDescription: str = ""
    lastOnline: Optional[str] = None


@dataclass
class ApiError:
    code: int
    message: str
    userFacingMessage: str


@dataclass
class Config:
    usernames: Dict[str, str]
    loggedIn: bool
    cookie: str

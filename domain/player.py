from .song import Song
from enum import Enum

class PlayerState(Enum):
    STOPPED = 0
    PLAYING = 1
    PAUSED = 2

class Player:
    def load(self, song: Song):
        pass
    def play(self):
        pass
    def resume(self):
        pass
    def pause(self):
        pass
    def stop(self):
        pass
    def seek(self, time: float):
        pass
    def pos(self) -> float:
        pass
    def duration(self) -> float:
        pass

class PlayMode(Enum):
    NORMAL = 0
    SHUFFLE = 1
    REPEAT = 2
    WEIGHTED = 3

class Playlist(list):
    index: int
    def __init__(self, songs: list[Song], mode: PlayMode = PlayMode.NORMAL):
        super().__init__(songs)
        self.mode = mode
    
    def next(self) -> Song:
        pass

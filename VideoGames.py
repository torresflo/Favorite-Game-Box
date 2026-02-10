import os
import json
import random

class VideoGame(object):
    def __init__(self, name: str, developer: str, releaseDate: str, description: str, platforms):
        self.m_name = name
        self.m_developer = developer
        self.m_releaseDate = releaseDate
        self.m_description = description
        self.m_platforms = platforms

    def __repr__(self) -> str:
        return f"<VideoGame {self.m_name}, released {self.m_releaseDate} by {self.m_developer}>"

class VideoGameList(object):
    DefaultDataFolder = "./data"
    DefaultDataFileName = f"{DefaultDataFolder}/games.json"
    
    def __init__(self):
        self.loadDataFromFile(VideoGameList.DefaultDataFileName)

    def loadDataFromFile(self, fileName: str):
        if os.path.exists(fileName):
            with open(fileName, "r", encoding="utf-8") as file:
                self.m_data = json.load(file)

    def getRandomVideoGame(self):
        if self.m_data is not None:
            randomVideoGame = random.choice(self.m_data["games"])
            return VideoGame(randomVideoGame["name"], randomVideoGame["developer"], randomVideoGame["releaseDate"], randomVideoGame["description"], randomVideoGame["platforms"])
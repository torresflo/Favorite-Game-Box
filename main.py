import os

from VideoGames import VideoGameList
from FileManager import FileManager

if __name__ == '__main__':
    videoGameList = VideoGameList()
    randomVideoGame = videoGameList.getRandomVideoGame()

    fileName = os.getenv("MARKDOWN_FILE")
    if fileName is not None:
        FileManager.writeRandomVideoGameInFile(fileName, randomVideoGame)
    else:
        raise Exception(f"Cannot find environment variable: MARKDOWN_FILE")

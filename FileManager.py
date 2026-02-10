import os

from VideoGames import VideoGame

class FileManager:
    FavoriteGameBoxStartString = "<!-- favorite-game-box start -->"
    FavoriteGameBoxEndString = "<!-- favorite-game-box end -->"
    DefaultReadmeFileName = "README.md"

    def writeRandomVideoGameInFile(fileName: str, videoGame: VideoGame):
        if os.path.exists(fileName):
            contentToWrite = FileManager.computeFileContentWithVideoGame(fileName, videoGame)
            with open(fileName, "w", encoding="utf-8") as file:
                file.write(contentToWrite)
        else:
            raise Exception(f"Cannot find file: {fileName}")

    def computeFileContentWithVideoGame(fileName: str, videoGame: VideoGame) -> str:
        with open(fileName, "r", encoding="utf-8") as file:
            content = file.read()

            startLineNumber = content.find(FileManager.FavoriteGameBoxStartString)
            endLineNumber = content.find(FileManager.FavoriteGameBoxEndString)

            before = content[0:startLineNumber]
            after = content[endLineNumber:len(content)]
            
            newContent = before
            newContent += FileManager.computeVideoGameString(videoGame)
            newContent += after
            return newContent

    def computeVideoGameString(videoGame : VideoGame) -> str:
        string = f"{FileManager.FavoriteGameBoxStartString}\n"
        string += '<div style="border:1px solid #30363d; border-radius:8px; padding:24px; background:#0d1117;">\n'
        string += f"<h2>{videoGame.m_name}</h2>\n"
        string += f"<strong>📅 Release</strong><br/>{videoGame.m_releaseDate}\n"
        string += f"<strong>🏗️ Developer</strong><br/>{videoGame.m_developer}\n"
        string += f"<strong>📖 Description</strong><br/>{videoGame.m_description}\n"
        string += '</div>\n'
        string += "<!-- Powered by https://github.com/torresflo/Favorite-Game-Box. -->\n"
        return string
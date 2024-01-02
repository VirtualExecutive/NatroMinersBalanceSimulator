import os

class Saver:
    LOGS_FOLDER_PATH="Logs"

    def __init__(self,miktar:float,days:int) -> None:
        Saver.CheckFolders()

        self.filename = f"{Saver.LOGS_FOLDER_PATH}\\"
        self.filename += f"{miktar}-{days}.log"
        
        with open(self.filename,"w") as f:
            pass

    def Write(self, text):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(text+"\n")

    def CheckFolders():
        if not os.path.exists(Saver.LOGS_FOLDER_PATH):
            os.makedirs(Saver.LOGS_FOLDER_PATH)
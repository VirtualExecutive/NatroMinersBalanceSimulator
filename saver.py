

class Saver:
    def __init__(self,miktar:float,days:int,MLCode=0) -> None:
        self.filename = f"{miktar}-{days}-{MLCode}.log"
        with open(self.filename,"w") as f:
            pass

    def Write(self, text):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(text+"\n")

from saver import *
from datetime import datetime, timedelta

class Package:
    doSave=False
    saver:Saver
    days=0
    selectedDays :int

    min_price :int
    max_price :int
    profit:dict

    balance: float
    winnedBalance =0.0

    def SelectDays(self, selectDays: int):
        self.selectedDays = selectDays
        return self

    def SetBalance(self, balance :float):
        self.balance = balance
        return self

    def SetDays(self, day:int):
        self.days = day
        return self
    
    def SetDate(self, date:datetime):
        self.days = (datetime.now() - date).days
        return self

    def SpentDay(self, language="EN")-> float:
        """
        EN
        ---
        Returns True if the number of days received from the user is reached.
        
        ---
        TR
        ---
        Simulatorde 1 gün zaman geçmesini sağlar. \n
        Yapılan işlemler:
        + 

        ---
        ```py
        return days==inputUserDays
        ```
        """
        self.days+=1
        profit = self.GetProfit()
        self.AddWinnedBalance(profit)
        if self.doSave:
            self.saver.Write(self.GetLogDaily(language))
        if(not self.isFinished()):
            return profit
        else:
            return profit+self.balance
    
    def FakeSpentDay(self):
        profit = self.GetProfit()
        self.AddWinnedBalance(profit)
    
    def AddWinnedBalance(self, amount:float)->None:
        """
        EN
        ---
        Adds to the total profit value.
        
        ---
        TR
        ---
        Toplam kazanç değerine ekleme yapar.

        ---
        ```py
        return None
        ```
        """
        self.winnedBalance+=amount

    def GetLogDaily(self, language="EN") ->str:
        """
        EN
        ---
        Returns the log of daily profit.
        
        ---
        TR
        ---
        Günlük logunu dönderir.

        ---
        
        ```py
        str="Package |  Days:9/90 | Amount:10.00$ | Daily Profit: 0.08$ (%0.75) | Total Profit:0.68$"
        return str
        ```
        """
        match language:
            case "EN":
                return f"Package |  Days:{self.days}/{self.selectedDays} | Amount:{self.balance:.2f}$ | Daily Profit: {self.GetProfit():.2f}$ (%{self.profit[str(self.selectedDays)]}) | Total Profit:{self.winnedBalance:.2f}$"
            case "TR":
                return f"Paket |  Gün:{self.days}/{self.selectedDays} | Miktar:{self.balance:.2f}$ | Günlük Kazanç: {self.GetProfit():.2f}$ (%{self.profit[str(self.selectedDays)]}) | Toplam Kazanç:{self.winnedBalance:.2f}$"
            case _:
                return f"Package |  Days:{self.days}/{self.selectedDays} | Amount:{self.balance:.2f}$ | Daily Profit: {self.GetProfit():.2f}$ (%{self.profit[str(self.selectedDays)]}) | Total Profit:{self.winnedBalance:.2f}$"
    
    def GetProfit(self)-> float:
        """
        EN
        ---
        Returns the value of daily profit.
        
        ---
        TR
        ---
        Günlük kar değerini döndürür.

        ---
        40$ and 120 days\n
        40 * (profit["120"]/100)
        ```py
        return float
        ```
        """
        return self.balance * (self.profit[str(self.selectedDays)]/100)

    def isFinished(self) -> bool:
        """
        EN
        ---
        Returns True if the number of days received from the user is reached.
        
        ---
        TR
        ---
        Eğer ki kullanıcıdan alınan gün sayısına ulaşılmış ise True dönderir.

        ---
        ```py
        return days==inputUserDays
        ```
        """
        return self.days == self.selectedDays

class Core10(Package):
    min_price = 10
    max_price = 1998
    profit={
        "30":0.55,
        "60":0.65,
        "90":0.75,
        "120":1.00,
        "365":0.50
    }

class Core16(Package):
    min_price = 2000
    max_price = 7498
    profit={
        "30":0.60,
        "60":0.70,
        "90":0.85,
        "120":1.25
    }

class Core24(Package):
    min_price = 7500
    max_price = 49999
    profit={
        "30":0.70,
        "60":0.80,
        "90":1.00,
        "120":1.50
    }

class Core36(Package):
    min_price = 50002
    max_price = 499999
    profit={
        "30":0.90,
        "60":1.00,
        "90":1.20,
        "120":2.00
    }

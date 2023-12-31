from saver import *
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

    def SpentDay(self)-> float:
        self.days+=1
        profit =  self.balance * (self.profit[str(self.selectedDays)]/100)
        self.winnedBalance+=profit
        if self.doSave:
            self.saver.Write(f"Paket:  Gün:{self.days}/{self.selectedDays} Miktar:{self.balance:.2f} Günlük Kar: {profit:.2f}(%{self.profit[str(self.selectedDays)]}) Toplam kar:{self.winnedBalance:.2f}")
        if(self.days<self.selectedDays):
            return profit
        else:
            return profit+self.balance
            

    def isFinished(self):
        return self.days == self.selectedDays

class Core10(Package):
    min_price = 10
    max_price = 1998
    profit={
        "30":0.55,
        "60":0.65,
        "90":0.75,
        "120":1.00
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

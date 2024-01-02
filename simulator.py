from packages import *
from saver import *

from datetime import datetime, timedelta

class Simulator:
    days = 0
    balance = 0.0
    packages = []
    saver=None
    date:datetime


    PACKAGES=[Core10,Core16,Core24,Core36]

    def __init__(self, balance:float=None, days:int=None ,doSave=False,language="EN") -> None:
        
        self.date = datetime.now()

        self.doSave = doSave
        self.language = language

        if not balance and not days:
            self.Start()
        else:
            self.invest =balance
            self.balance = self.invest 
            self.u_days = days
        
        self.CustomPackages()
        
        if doSave:
            self.saver = Saver(self.balance,self.u_days)
            for package in self.packages:
                package.saver = self.saver

        
        self.Div()
        self.Loop()

    def CustomPackages(self):
        packages = [
            Core10().SelectDays(365).SetBalance(10).SetDate(datetime(2023,11,10)),
            Core10().SelectDays(120).SetBalance(20).SetDate(datetime(2023,11,24)),
            Core10().SelectDays(120).SetBalance(18).SetDate(datetime(2023,12,11)),
            Core10().SelectDays(120).SetBalance(40).SetDate(datetime(2023,12,29))

        ]

        for package in packages:
            for i in range(package.days):
                package.FakeSpentDay()
            package.doSave = self.doSave
            self.packages.append(package)

    def Div(self):
        if self.doSave:
            self.saver.Write("-"*30)

    def Start(self):
        investAsk=""
        daysAsk=""
        match self.language:
            case "EN":
                investAsk="Enter the starting USD amount:"
                daysAsk="How many days? : "
                havePackAsk="Do you have packages?(Y/N): "
            case "TR":
                investAsk="Başlangıç USD miktarını giriniz: "
                daysAsk="Kaç gün sürecek? : "
                havePackAsk="Herhangi bir pakete sahip misiniz?(Y/N): "
            case _:
                investAsk="Enter the starting USD amount:"
                daysAsk="How many days? : "
                havePackAsk="Do you have packages?(Y/N): "
        self.invest = float(input(investAsk))
        self.balance = self.invest
        self.u_days = int(input(daysAsk) )
        self.havePackage = input(havePackAsk).lower()

        
        if self.havePackage in ["y","n"]:
            if self.havePackage == "y":
                match self.language:
                    case "EN":
                        pass
                    case "TR":
                        coreAsk="Core: "
                        investAsk="Yatırım: "
                        daysAsk="Gün: "
                        profitAsk="Kazanılan Kar:"
                    case _:
                        pass
                while(True):
                    try:
                        core = int(input(coreAsk))
                    except:
                        print("Hesaplanılıyor.")
                        break
                    days = int(input(daysAsk))
                    invest = int(input(investAsk))
                    profit = float(input(profitAsk))
                    
                    match core:
                        case 10:
                            package = Core10()
                        case 16:
                            package = Core16()
                        case 24:
                            package = Core24()
                        case 36:
                            package = Core36()
                    
                    package:Core10
                    package.SelectDays(days).SetBalance(invest)
                    spentDays =  profit / (invest * (package.profit[str(days)]/100))
                    spentDays = int(f"{spentDays:.0f}")

                    package.days = spentDays
                    package.doSave = self.doSave

                    self.packages.append(package)



            elif self.havePackage =="n":
                pass
        else:
            print("Geçersiz yanıt. Paketsiz hesaplama yapılıyor.")


    def Loop(self):
        while(self.days<self.u_days):
            if self.isBalanceBiggerThan10():
                self.BuyNewPackage()
            self.SpentDay()
            self.DeleteFinishedPackages()
            self.Div()
        if self.doSave:
            self.saver.Write("Bakiye: " + f"{self.balance:.2f}")

    def SetBalance(self, balance:float):
        self.balance = balance
        return self
    
    def SetDays(self, days:int):
        self.days = days
        return self
    
    def isBalanceBiggerThan10(self):
         return 10.0 <= self.balance
    
    def SpentDay(self):
        self.date = self.date + timedelta(days=1)
        self.days+=1
        self.Div()
        if self.doSave:
            match self.language:
                case "EN":
                    self.saver.Write(f"Day: {self.days}  Date: {self.date.date()}     Amount:{self.balance:.2f}       Daily Profit:{(sum( package.balance * (package.profit[str(package.selectedDays)]/100)for package in self.packages)):.2f}")
                case "TR":
                    self.saver.Write(f"Gün: {self.days}  Tarih: {self.date.date()}      Bakiye:{self.balance:.2f}       Günlük Kar:{(sum( package.balance * (package.profit[str(package.selectedDays)]/100)for package in self.packages)):.2f}")
                case _:
                    self.saver.Write(f"Day: {self.days}  Date: {self.date.date()}     Amount:{self.balance:.2f}       Daily Profit:{(sum( package.balance * (package.profit[str(package.selectedDays)]/100)for package in self.packages)):.2f}")

        for package in self.packages:
            self.balance+=package.SpentDay(self.language)

    def DeleteFinishedPackages(self):
        toRemovePackages = []
        for package in self.packages:
            package:Package
            if package.isFinished():
                toRemovePackages.append(package)
                if self.doSave:
                    match self.language:
                        case "EN":
                            self.saver.Write(f"Package finished:  Day: {package.selectedDays} Invest: {package.balance:.2f} Profit:{package.winnedBalance:.2f} Total Profit: {(package.balance+package.winnedBalance):.2f}")
                        case "TR":
                            self.saver.Write(f"Paket bitti:  Gün: {package.selectedDays} Yatırılan: {package.balance:.2f} Kar:{package.winnedBalance:.2f} Kazanç: {(package.balance+package.winnedBalance):.2f}")
                        case _:
                            self.saver.Write(f"Package finished:  Day: {package.selectedDays} Invest: {package.balance:.2f} Profit:{package.winnedBalance:.2f} Total Profit: {(package.balance+package.winnedBalance):.2f}")                            
        
        for package in toRemovePackages:
            self.packages.remove(package)

    def BuyNewPackage(self):
        for package in self.PACKAGES[::-1]:
            package:Package
            if package.min_price <= self.balance and self.balance <= package.max_price:
                if 120<=self.u_days-self.days:
                    selectDay = 120
                elif 90<=self.u_days-self.days:
                    selectDay = 90
                elif 60<=self.u_days-self.days:
                    selectDay = 60
                elif 30<=self.u_days-self.days:
                    selectDay = 30
                else:
                    return
                package_:Package
                cent = self.balance %1
                self.balance = self.balance - cent
                package_ = package().SetBalance(self.balance).SelectDays(selectDay)
                package_.doSave = self.doSave
                package_.saver = self.saver
                self.packages.append(package_)
                if self.doSave:
                    match self.language:
                        case "EN":
                            self.saver.Write(f"Added Package: Day:{selectDay} Amount: {self.balance:.2f}  Daily Profit: {(self.balance * package_.profit[str(package_.selectedDays)]/100):.2f}({(package_.profit[str(package_.selectedDays)]):.2f})")
                        case "TR":
                            self.saver.Write(f"Yeni paket eklendi: Gün:{selectDay} Miktar: {self.balance:.2f}  Günlük Kar: {(self.balance * package_.profit[str(package_.selectedDays)]/100):.2f}({(package_.profit[str(package_.selectedDays)]):.2f})")
                        case _:
                            self.saver.Write(f"Added Package: Day:{selectDay} Amount: {self.balance:.2f}  Daily Profit: {(self.balance * package_.profit[str(package_.selectedDays)]/100):.2f}({(package_.profit[str(package_.selectedDays)]):.2f})")
                            
                self.balance=cent

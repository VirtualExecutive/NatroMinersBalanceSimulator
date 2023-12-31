from packages import *
from saver import *

class Simulator:
    days = 0
    balance = 0.0
    packages = []
    saver=None

    isML=False

    PACKAGES=[Core10,Core16,Core24,Core36]

    def __init__(self, balance:float=None, days:int=None ,doSave=False,combination:list=None, MLCode=0) -> None:
        if combination:
            self.isML=True
            self.combination = combination

        self.doSave = doSave
        if doSave:
            self.saver = Saver(balance,days,MLCode)

        if not balance and not days:
            self.StartUp()
        else:
            self.invest =balance
            self.balance = self.invest 
            self.u_days = days

        self.Loop()

    def Div(self):
        if self.doSave:
            self.saver.Write("-"*30)

    def StartUp(self):
        self.invest = float(input("Başlangıç USD miktarını giriniz: "))
        self.balance = self.invest
        self.u_days = int(input("Kaç gün sürecek? : ") )
        self.Div()

    def Loop(self):
        while(self.days<self.u_days):
            if self.isBalanceBiggerThan10():
                if self.isML:
                    if self.combination[self.days]:
                        self.BuyNewPackage()
                else:
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
        self.days+=1
        self.Div()
       
        if self.doSave:
            self.saver.Write(f"Gün: {self.days}       Bakiye:{self.balance:.2f}       Günlük Kar:{(sum( package.balance * (package.profit[str(package.selectedDays)]/100)for package in self.packages)):.2f}")

        for package in self.packages:
            package : Package
            self.balance+=package.SpentDay()

    def DeleteFinishedPackages(self):
        toRemovePackages = []
        for package in self.packages:
            package:Package
            if package.isFinished():
                toRemovePackages.append(package)
                if self.doSave:
                    self.saver.Write(f"Paket bitti:  Gün: {package.selectedDays} Yatırılan: {package.balance:.2f} Kar:{package.winnedBalance:.2f} Kazanç: {(package.balance+package.winnedBalance):.2f}")
        
        for package in toRemovePackages:
            self.packages.remove(package)

    def BuyNewPackage(self):
        for package in self.PACKAGES[::-1]:
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
                package_ = package().SetBalance(self.balance).SelectDays(selectDay)
                package_.doSave = self.doSave
                package_.saver = self.saver
                self.packages.append(package_)
                if self.doSave:
                    self.saver.Write(f"Yeni paket eklendi: Gün:{selectDay} Miktar: {self.balance:.2f}  Günlük Kar: {(self.balance * package_.profit[str(package_.selectedDays)]/100):.2f}({(package_.profit[str(package_.selectedDays)]):.2f})")
                self.balance=0.0


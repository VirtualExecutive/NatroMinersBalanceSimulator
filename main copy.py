from simulator import Simulator
from itertools import product
from concurrent.futures import ThreadPoolExecutor

if __name__=="__main__":
        input = Simulator()
        invest = input.invest
        u_days = input.u_days
        
        
        combinations = []
        lastDaysBlock = 29
        count = 0
        countLen = 2**(u_days-lastDaysBlock-1)
                
        best_comb:list
        best_balance=0

        def tryCombination(combination,MLCode):
                global count,best_balance,best_comb
                #count+=1
                #print(f"{(count/countLen)*100:.8f}")
                sim = Simulator(balance=invest, days=u_days, combination=combination)
                if best_balance < sim.balance:
                        best_balance = sim.balance
                        best_comb = combination
                        print("En iyi kombinasyon bulundu. ", best_balance, best_comb)
                        Simulator(balance=invest, days=u_days, doSave=True, combination=best_comb,MLCode=MLCode)

        # with ThreadPoolExecutor(max_workers=1) as tp: 
        #     mlcode =0
        #     for combination in product([1,0], repeat=u_days-lastDaysBlock):
        #         if(mlcode==4):
        #                mlcode=1
        #         else:
        #                mlcode+=1
        #         if combination[0] ==0:
        #                break
        #         tp.submit(tryCombination, list(combination)+[0]*29, mlcode)
            
        #     tp.shutdown()

        for combination in product([1,0], repeat=u_days-lastDaysBlock):
                tryCombination(combination=list(combination)+[0]*29,MLCode=0)
        
        Simulator(balance=invest, days=u_days, doSave=True, combination=best_comb)
from simulator import Simulator
if __name__=="__main__":
        while(True):
                input = Simulator()
                invest = input.invest
                u_days = input.u_days

                Simulator(invest,u_days,True)
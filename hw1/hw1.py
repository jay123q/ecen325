# %%
import numpy as np
import matplotlib.pyplot as plt
import control
#Joshua Clapp ecen 325

def main():
    Hw = -400000*control.tf([1,0],[1,2000200 , (20000**2)])
    print(Hw)
    mag,phase,omega = control.bode(Hw)
    pass
#Joshua Clapp ecen 325
if( __name__ == "__main__"):
    main()
    
# %%

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter



def draw_diagram(month,temp,prec):

    month = ["%.2f" % number for number in month]
    month[0] = "JAN"
    month[1] = "FEB"
    month[2] = "MAR"
    month[3] = "APR"
    month[4] = "MAY"
    month[5] = "JUN"
    month[6] = "JUL"
    month[7] = "AUG"
    month[8] = "SEP"
    month[9] = "OCT"
    month[10] = "NOV"
    month[11] = "DEC"

    """i = 0
    while i < len(prec):
        prec[i] = float(prec[i])/2.0
        i+=1"""
    
    fig, x1= plt.subplots()

    x1.set_xlabel("Months")
    x1.set_ylabel("Temperature in °C")
    x1.plot(month, temp, c = '#ff0000')
    x1.tick_params(axis='y')


    

    x2 = x1.twinx() #TODO make both y axis the same range so that y axis of temperature is always half as big as 2nd y axis

    """def millions(x, pos):
        return x*2

    formatter = FuncFormatter(millions)
    x2.yaxis.set_major_formatter(formatter)"""

    x2.set_ylabel("Precipitation in mm")
    x2.plot(month, prec, color='#0000ff')
    x2.tick_params(axis='y')


    plt.title("Climate diagram")
    plt.grid(True, linestyle=(0, (1, 10)), )
    
    x1.fill_between(month, temp, prec, where=(temp > prec), color='#ff0000', alpha=0.3,interpolate=True)
    x1.fill_between(month, temp, prec, where=(temp <= prec), color='#0000ff', alpha=0.3,interpolate=True)
    fig.tight_layout()

    plt.show()
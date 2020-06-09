import pandas as pd
from tkinter import messagebox
import numpy





def file_read(path, csv, xlsx):
    
    
    if csv == True and xlsx == True:
        messagebox.showerror("ERROR", "Bitte waehlen Sie nur 1 Datentyp aus")
    elif csv == True:
        data = pd.read_csv(path,usecols=['month','temp','prec'])
    elif xlsx == True:
        data = pd.read_xlsx(path)
    else:
        messagebox.showerror("ERROR", "Bitte waehlen Sie einen Datentyp aus")

    
    
    data=data.to_numpy()

    month = data[:,0]
    temp = data[:,1]
    prec = data[:,2]


    return month,temp,prec


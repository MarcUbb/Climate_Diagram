from tkinter import *
import read
import plot

def process():
    plot.draw_diagram(read.file_read(path.get(),c.get(),x.get())[0],read.file_read(path.get(),c.get(),x.get())[1],read.file_read(path.get(),c.get(),x.get())[2])


window = Tk()

window.title("Climate Diagram")
window.geometry('300x150')
window.wm_iconbitmap('icon.ico')

c = IntVar()
x = IntVar()

Ltype = Label(window, text="Dateityp")
type_csv = Checkbutton(window, text=".csv", variable=c)
type_xlsx = Checkbutton(window, text=".xlsx", variable=x)


Lpath = Label(window, text="Dateipfad")
path = Entry(window)


enter = Button(window, text="plot", command = process)

Ltype.pack()
type_csv.pack()
type_xlsx.pack()

Lpath.pack()
path.pack()

enter.pack()
window.mainloop()
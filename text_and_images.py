from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack()
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground='blue', background='yellow')
label.config(font=('Courier', 18, 'bold'))

logo = PhotoImage(file="C:\\Users\\Paopao\\Pictures\\Python.gif")
label.config(image = logo)
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')

if __name__ == '__main__':
    mainloop()

import time
import tkinter

master = tkinter.Tk()

words = tkinter.Message(master, text="Hello World")
words.pack()

master.after(5000, master.destroy)
tkinter.mainloop()

master = tkinter.Tk()

words = tkinter.Message(master, text="Hello World Again")
words.pack()

master.after(5000, master.destroy)
master.mainloop()

master = tkinter.Tk()

words = tkinter.Message(master, text="Hello World Once More")
words.pack()

master.after(5000, master.destroy)
tkinter.mainloop()
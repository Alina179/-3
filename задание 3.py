from tkinter import *

OPTIONS = [
"Январь",
"Февраль",
"Март",
"Апрель",
"Май",
"Июнь",
] #etc

master = Tk()
master.title("Задание 3")
master.geometry("300x100")
master["bg"] = "Pink"
variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

mainloop()

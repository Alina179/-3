from tkinter import *
languages = [("Лак для волос",1 ), ("Шампунь", 2), ("Мыло", 3), ("Пена для бритья", 4), ("Зубная паста", 5), ("Зубная щётка", 6)]
def select():
    l = language.get()
    if l == 1:
     sel.config(text="Цена: 150 руб.")
    elif l == 2:
     sel.config(text="Цена: 100 руб.")
    elif l == 3:
     sel.config(text="Цена:50 руб.")
    elif l == 4:
     sel.config(text="Цена: 200 руб.")
    elif l == 5:
     sel.config(text="Цена: 100 руб.")
    elif l == 6:
     sel.config(text="Цена: 40 руб.") 

root = Tk()
root.title("Пример 13")
root.geometry("500x380")
root["bg"] = "Snow"
header = Label(text="Выберите товар", padx=15, pady=10,  bg='Snow',font= "11",)
header.grid(row=0, column=0, sticky=W)
language = IntVar()
row = 1
for txt, val in languages:
	Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, bg='Snow', command=select)\
    	.grid(row=row, sticky=W)
	row += 1
sel = Label(padx=15, pady=10 )
sel.grid(row=row, sticky=W)

root.mainloop()

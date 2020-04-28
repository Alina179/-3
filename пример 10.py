from tkinter import *
from tkinter import messagebox
 
def display_full_name():
	messagebox.showinfo("Окно сообщения", name.get() + " " + surname.get())
 
root = Tk()
root.title("Пример 10")
root.geometry('250x150')
root["bg"] = "White"
name = StringVar()
surname = StringVar()
 
name_label = Label(text="Введите имя:",bg = "White" )
surname_label = Label(text="Введите фамилию:", bg = "White" )
 
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
 
name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
 
name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)
 
message_button = Button(text="Показать", bg = "White",command=display_full_name)
message_button.grid(row=6,column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()

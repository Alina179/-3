
import tkinter as tk
 
window = tk.Tk()
window.title('Пример (12)')
window.geometry('250x150')
window["bg"] = "White"

l = tk.Label(window, bg='Pink', width=60, font= "11",  text='Ничего не выбрано')
l.pack()

def print_selection():
        if (var1.get() == 1) & (var2.get() == 0):
         l.config(text='Мне нравится python', )
        elif (var1.get() == 0) & (var2.get() == 1):
         l.config(text='Мне нравится C++',)
        elif (var1.get() == 0) & (var2.get() == 0):
         l.config(text='Мне ничего не нравится', )
        else:
         l.config(text='Мне нравятся оба языка',)
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, bg='White',font= "10", fg="DeepPink", command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, bg='White',font= "10", fg="DeepPink", command=print_selection)
c2.pack()
 
window.mainloop()

 

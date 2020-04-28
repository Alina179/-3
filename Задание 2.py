from tkinter import *
root = Tk()
root.title("Задание 2")
root.geometry("400x250")
root["bg"] = "Pink"
main_menu = Menu()

file_menu = Menu(font=("Times New Roman", 12),activebackground= "Coral", activeborderwidth= 4)
file_menu.add_command(label="Новый")
file_menu.add_command(label="Открыть...")
file_menu.add_command(label="Сохранить...")
file_menu.add_command(label="Выход")
file_menu.add_separator()

help_menu = Menu(font=("Times New Roman", 12),activebackground= "Coral", activeborderwidth= 4)
help_menu.add_command(label="Помощь")
help_menu.add_command(label="О программе")
help_menu.add_separator()

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка" ,menu=help_menu)
root.config(menu=main_menu)
root.mainloop()

from tkinter import *
from tkinter import messagebox

message_write = None

# Hello = "Здраствуйте ,"
#
# Data = "Ваши данные сохраннены"

w_n = 0


def show_message():
    global message_write
    global w_n
    message_write = message.get()
    messagebox.showinfo("ВНИМАНИЕ!!!", message="Здравствуйте, %s" % message_write)
    file = open("D:\Новая папка\path.txt", 'a+')
    file.write(message_write)
    root.destroy()
    canvas_root = Tk()
    canvas_root.resizable(0, 0)
    canvas_root.title("ВИКТОРИНА")
    canvas2 = Canvas(canvas_root, width=1300, height=700)
    canvas2.pack()
    сanvas2.create_image(0, 0, image=PhotoImage(file="D:\Новая папка\Задание 1.gif"))


root = Tk()
root.resizable(0, 0)
root.title("ВИКТОРИНА")
root.geometry("1300x700")

message = StringVar()

message_entry = Entry(textvariable=message, font="arial 60")
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Начать тест", command=show_message, font="arial 60")
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()

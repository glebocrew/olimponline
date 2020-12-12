from tkinter import *
from tkinter import messagebox
import time
import re
import user_manager as um

message_write = None

# Hello = "Здраствуйте ,"
#
# Data = "Ваши данные сохраннены"

# RES_PATH = "D:\\USERDATA\\Gleb\\Python\\olimponline\\res\\"
RES_PATH = ".\\res\\"


def start_session():

    if um.check_user(username.get(), password.get()):
        pass
        # messagebox.showinfo("ВНИМАНИЕ!!!", message="Логин или пароль верен!")
    else:
        messagebox.showinfo("ВНИМАНИЕ!!!", message="Логин или пароль неверен!")
        return

    messagebox.showinfo("ВНИМАНИЕ!!!", message="Здравствуйте, %s" % username.get())
    file = open("log/programm.log.txt", 'a+')
    file.write(username.get() + " Вошёл(ла) в систему в %s" % time.strftime("%c") + "\n")
    root.destroy()
    canvas_root = Tk()
    canvas_root.resizable(0, 0)
    canvas_root.title("ВИКТОРИНА")
    canvas2 = Canvas(canvas_root, width=1300, height=700)
    canvas2.pack()
    canvas_root.update()
    task_image = PhotoImage(file=RES_PATH + "question 1.gif")
    canvas2.create_image(0, 0, anchor=NW, image=task_image)
    canvas2.pack()
    answer = StringVar()
    # answer_entry = Entry(textvariable=answer, font="arial 30")
    # answer_entry.place(relx=.400, rely=.800, anchor="c")
    # def check():
    #     if answer.get() == "Б" or answer.get() == "б":
    #         file.write("\nRight!")
    #     else:
    #         file.write("\nWrong!")
    # answer_button = Button(canvas_root,text="Ответить", command=check, font="arial 30")
    # answer_button.pack()
    # canvas_root.mainloop()
    canvas2.create_text(300, 800, text="ОТВЕТ", font="Arial 30")
    # check()
    canvas_root.update()
    canvas_root.mainloop()


root = Tk()
root.resizable(0, 0)
root.title("ВИКТОРИНА")
root.geometry("1300x700")

username = StringVar()
message_entry = Entry(textvariable=username, font="arial 30")
message_entry.place(relx=.5, rely=.1, anchor="c")

password = StringVar()
message_entry = Entry(textvariable=password, font="arial 30")
message_entry.place(relx=.5, rely=.2, anchor="c")

message_button = Button(text="Войти", command=start_session, font="arial 30")
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()



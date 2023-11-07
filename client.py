import socket
from tkinter import *

def btn_click_ip():
    global client
    ip = IpInput.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 12345))
    client.send("button".encode("utf-8"))
    data = client.recv(1024).decode("utf-8")
    if data == "OK":
        title.config(text="Cоединение установлено!", bg='white')
        btn1.grid()
    print(ip, 'connect')

def btn_youtube():
    client.send("youtube".encode("utf-8"))


root = Tk()
root['bg'] = '#7f7679'
root.title('Клиент')
root.wm_attributes('-alpha', 0.95)
root.geometry('600x600')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=600, width=600)
canvas.pack()

frame = Frame(root, bg='#828282')
frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

IpInput = Entry(frame, bg='white', font = 40, justify = CENTER)
IpInput.pack()

title = Label(frame, text="Соединение не установлено!", bg='white', font=40)
title.pack()

btn1 = Button(frame, text='Подключиться к серверу', bg='white', height=10, width=30, command=btn_click_ip)
btn1.pack()

btn2 = Button(frame, text='Ютуб', bg='white', height=10, width=30, command=btn_youtube)
btn2.pack()

root.mainloop()
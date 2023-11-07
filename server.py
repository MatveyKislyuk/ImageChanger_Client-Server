import socket
import tkinter
import webbrowser
from tkinter import *
import threading
from PIL import Image, ImageTk

def socket_thread():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostbyname(socket.gethostname()), 12345))
    print(socket.gethostbyname(socket.gethostname()), 'Сервер запущен')
    server.listen()
    flag = 1

    while True:
        user, adres = server.accept()

        while True:
            data = user.recv(1024).decode("utf-8").lower()

            if data == "button":
                print("Соединение установлено!")
                message = "OK"
                user.send(message.encode("utf-8"))
            if data == "youtube":
                image_path1 = 'images/1.jpg'
                image_path2 = 'images/2.jpg'
                image_path3 = 'images/3.jpg'
                image1 = Image.open(image_path1)
                image2 = Image.open(image_path2)
                image3 = Image.open(image_path3)
                photo1 = ImageTk.PhotoImage(image1)
                photo2 = ImageTk.PhotoImage(image2)
                photo3 = ImageTk.PhotoImage(image3)
                if flag == 1:
                    label.config(image=photo2)
                    flag = 2
                elif flag == 2:
                    label.config(image=photo3)
                    flag = 3
                else:
                    label.config(image=photo1)
                    flag = 1


def main_thread():
    global label
    root = Tk()
    root['bg'] = '#7f7679'
    root.title('Сервер')
    root.wm_attributes('-alpha', 0.95)
    root.geometry('600x600')
    root.resizable(width=False, height=False)

    canvas = Canvas(root, height=600, width=600)
    canvas.pack()

    frame = Frame(root, bg='#828282')
    frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

    title = Label(frame, text=socket.gethostbyname(socket.gethostname()), bg='white', font=40)
    title.pack()

    frame2 = Frame(frame, bg='black')
    frame2.place(relx=0.136, rely=0.136, relwidth=0.73, relheight=0.73)

    frame3 = Frame(frame, bg='white')
    frame3.place(relx=0.15, rely=0.15, relwidth=0.70, relheight=0.70)

    image_path = 'images/1.jpg'
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    label = Label(frame3, image=photo)
    label.image = photo  # нужно для изменения размера окна
    label.pack()

    root.mainloop()


socket_thread = threading.Thread(target=socket_thread)
main_thread = threading.Thread(target=main_thread)

socket_thread.start()
main_thread.start()

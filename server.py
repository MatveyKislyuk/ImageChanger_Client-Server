import socket
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk
from itertools import cycle
import os
import sys

class ImageChangerServer:
    def __init__(self, port):
        self.root = tk.Tk()
        self.root.title("Сервер")
        self.root.geometry("600x720")
        self.root.configure(bg='#E1D6F2')
        self.root.resizable(width=False, height=False)

        self.ip_label = tk.Label(self.root, text=f"Сервер IP: {self.get_server_ip()}", bd=1, relief="solid", height=2, width=25, font=("Arial", 14), bg='#F6F1FE')
        self.ip_label.pack(pady=20)

        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        self.image_paths = cycle([os.path.join(base_path, "images/1.jpg"), os.path.join(base_path, "images/2.jpg"), os.path.join(base_path, "images/3.jpg"), os.path.join(base_path, "images/4.jpg"), os.path.join(base_path, "images/5.jpg")])
        self.current_image_path = next(self.image_paths)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=0)

        self.load_and_display_image()

        self.server_socket = None
        self.accept_thread = None
        self.server_running = False

        self.start_button = tk.Button(self.root, text="Запуск сервера", height=2, width=21, bg='#BDAED2', font=("Arial", 14, "bold"), command=self.start_server)
        self.start_button.pack(pady=15)

        self.stop_button = tk.Button(self.root, text="Остановка сервера", height=2, width=21, bg='#BDAED2', font=("Arial", 14, "bold"), command=self.stop_server, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Обработка события закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def get_server_ip(self):
        return socket.gethostbyname(socket.gethostname())

    def accept_connections(self):
        while self.server_running:
            user, address = self.server_socket.accept()
            print(f"Cоединение с {address}")
            user_thread = Thread(target=self.handle_user, args=(user,))
            user_thread.start()

    def handle_user(self, user):
        while self.server_running:
            try:
                data = user.recv(1024).decode("utf-8").lower()
                if data == "change_image":
                    self.change_image()
            except Exception as e:
                print(f"Error handling user: {e}")
                break

    def load_and_display_image(self):
        try:
            image = Image.open(self.current_image_path)
            image = image.resize((500, 450))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error loading and displaying image: {e}")

    def change_image(self):
        try:
            self.current_image_path = next(self.image_paths)
            self.load_and_display_image()
        except Exception as e:
            print(f"Error changing image: {e}")

    def on_closing(self):
        self.stop_server()
        self.root.destroy()

    def start_server(self):
        if not self.server_running:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.get_server_ip(), 12345))
            self.server_socket.listen()

            self.server_running = True
            self.accept_thread = Thread(target=self.accept_connections)
            self.accept_thread.start()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_server(self):
        if self.server_running:
            self.server_running = False
            if self.server_socket:
                self.server_socket.close()
            if self.accept_thread:
                self.accept_thread.join()

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    server = ImageChangerServer(12345)
    server.run()

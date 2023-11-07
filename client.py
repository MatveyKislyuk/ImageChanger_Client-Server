import tkinter as tk
import socket
import os

class ImageChangerClient:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Клиент")
        self.root.geometry("400x250")
        self.root.configure(bg='#E1D6F2')

        self.server_ip_entry = tk.Entry(self.root, width=23, font=("Arial", 14), justify="center", bg='#F6F1FE')
        self.server_ip_entry.insert(0, "127.0.0.1")
        self.server_ip_entry.pack(pady=15)

        self.connect_button = tk.Button(self.root, text="Подключиться", height=2, width=21, bg='#BDAED2', font=("Arial", 14, "bold"), command=self.connect_to_server)
        self.connect_button.pack(pady=10)

        self.change_image_button = tk.Button(self.root, text="Сменить изображение", height=2, width=21, bg='#BDAED2', font=("Arial", 14, "bold"), command=self.send_change_image, state="disabled")
        self.change_image_button.pack(pady=10)

        self.client_socket = None

        self.load_connection_info()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load_connection_info(self):
        if os.path.exists("connection_info.txt"):
            with open("connection_info.txt", "r") as file:
                connection_info = file.read().split(":")
                if len(connection_info) == 2:
                    ip, port = connection_info
                    self.server_ip_entry.delete(0, tk.END)
                    self.server_ip_entry.insert(0, ip)

    def connect_to_server(self, port=None):
        server_ip = self.server_ip_entry.get()
        server_port = port or 12345

        if self.client_socket:
            self.client_socket.close()

        try:
            self.client_socket = socket.create_connection((server_ip, server_port), timeout=1)
            self.change_image_button.config(state="normal")

            with open("connection_info.txt", "w") as file:
                file.write(f"{server_ip}:{server_port}")
        except socket.timeout:
            print("Время вышло. Пожалуйста, проверьте IP и повторите попытку.")
        except ConnectionRefusedError as e:
            print(f"Ошибка подключения: {e}")

    def send_change_image(self):
        try:
            self.client_socket.send("change_image".encode("utf-8"))
        except Exception:
            self.connect_to_server()

    def on_closing(self):
        if self.client_socket:
            self.client_socket.close()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    client = ImageChangerClient()
    client.run()
import tkinter as tk

root = tk.Tk()

root.title("круть")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 600
window_height = 650
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

label1 = tk.Label(root, text="Это пример использования place()")
label1.place(x=300, y=50)

button1 = tk.Button(root, text="Поздоровайся", command=say_hello)
button1.place(x=250, y=100)

root.mainloop()






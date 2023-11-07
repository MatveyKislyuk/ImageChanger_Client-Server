<H1 align="center">ImageChanger_Client-Server</H1>

<H2>Version</H2> 

- **1.0 developer beta**

<H2>Description</H2>

- **ImageChangerServer** is a lightweight server application designed to facilitate real-time image changes. Developed by Matvey Kislyuk, this server allows multiple clients to connect and interactively update the displayed image.

<H2>Key Features</H2>

- Real-time display of the current image on the server.
- Seamless image change functionality triggered by connected clients.
- Support for multiple simultaneous client connections.
- Simple and intuitive interface.

<H2>Getting Started</H2>

1. Start the server by specifying the port (default is 12345).
2. Launch the client application, enter the server's IP address, and connect.
3. Use the client application to send a command to change the image.

<H2>Requirements</H2>

- Python 3.x
- Libraries: tkinter, socket, threading, PIL

<H2>Building an Executable File</H2>

1. To create an executable file (exe), use PyInstaller with the --onefile and --noconsole flags.
- **pyinstaller --onefile --noconsole server.py**
2. Ensure that the images are located in the images folder within the application directory before running.

<H2>Contribution</H2>

- Your contributions are welcome! Feel free to create enhancement requests and propose changes.


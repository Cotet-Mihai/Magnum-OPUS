import customtkinter as ctk
from Login.login import Login

if __name__ == '__main__':
    # Root Adj
    root = ctk.CTk()  # Root
    root._set_appearance_mode("Dark")  # Set appearance mode to Dark
    root.lift()  # We bring the window to the foreground
    root.iconbitmap('images/ICO/icon logo.ico')  # Icon Logo
    root.resizable(False, False)  # Window cant be resizable
    root.title("Magnum OPUS")  # Title

    Login(root)

    root.mainloop()  # Main loop for root

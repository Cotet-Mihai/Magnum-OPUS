import customtkinter as ctk
from Login.login import Login

if __name__ == '__main__':
    # Main Root
    main_root = ctk.CTk()

    # Main Root Adjustements
    main_root._set_appearance_mode("Dark")  # Set appearance mode to Dark
    main_root.lift()  # We bring the window to the foreground
    main_root.iconbitmap('images/ICO/icon logo.ico')  # Icon Logo
    main_root.resizable(False, False)  # Window cant be resizable
    main_root.title("Magnum OPUS")  # Title

    # Call Login
    Login(main_root)

    # Main loop for root
    main_root.mainloop()

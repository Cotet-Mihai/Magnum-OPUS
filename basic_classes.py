import customtkinter as ctk
from colors import Colors
from images.PNG.png import Images
from typing import List, Callable
from basic_functions import show_the_call


class LeftMenu:
    def __init__(self, root: ctk.windows.ctk_tk.CTk,
                 text_buttons: list[str] = None,
                 list_of_functions: List[Callable] = None) -> None:
        """
        :param root: need to bee ctk root
        :param text_buttons: it must contain the text of the 4 menu buttons
        :param list_of_functions: it must contain the functions of the 4 menu buttons
        """
        show_the_call(LeftMenu)

        # Root
        self.root = root

        # SPECIAL CASES
        # If text_buttons is None use this template
        if text_buttons is None:
            text_buttons = ['Button1', 'Button2', 'Button3', 'Button4']

        # If list_of_functions is None use this template
        if list_of_functions is None:
            list_of_functions = [lambda: print('Button 1 has been pressed'),
                                 lambda: print('Button 2 has been pressed'),
                                 lambda: print('Button 3 has been pressed'),
                                 lambda: print('Button 4 has been pressed')]

        # Set vars
        self.list_of_functions = list_of_functions
        self.text_buttons = text_buttons

        # Widgets
        self.widgets(self.text_buttons)

    def widgets(self, text_buttons: list[str]) -> None:

        """
        :param text_buttons: It must be a list of strings with the text that will be displayed on the buttons
        :return: Display all widgets for the left menu
        """

        # Main frame for left menu
        self.left_menu = ctk.CTkFrame(
            self.root,
            width=250,
            height=670,
            fg_color="white",
            corner_radius=15
        )
        self.left_menu.place(anchor='center', x=140, y=350)

        # Label containing the logo of the application
        self.logo_label = ctk.CTkLabel(
            self.left_menu,
            text="",
            image=Images.red_logo
        )
        self.logo_label.place(anchor='center', x=125, y=75)

        # Black line under the logo for design
        self.black_line = ctk.CTkFrame(
            self.left_menu,
            fg_color="#2b2b2b",
            width=180, height=2,
            corner_radius=2
        )
        self.black_line.place(anchor='n', x=125, y=150)

        # First Button
        self.button_one = ctk.CTkButton(
            self.left_menu,
            text=text_buttons[0],
            fg_color="white",
            hover_color=Colors.light_red,
            font=("Montserrat ExtraBold", 15),
            text_color="black",
            corner_radius=15,
            width=200, height=50,
            command=self.list_of_functions[0]
        )
        self.button_one.place(anchor='center', x=125, y=200)

        # Second Button
        self.button_two = ctk.CTkButton(
            self.left_menu,
            text=text_buttons[1],
            fg_color="white",
            hover_color=Colors.light_red,
            font=("Montserrat ExtraBold", 15),
            text_color="black",
            corner_radius=15,
            width=200, height=50,
            command=self.list_of_functions[1]
        )
        self.button_two.place(anchor='center', x=125, y=255)

        # Third Button
        self.button_three = ctk.CTkButton(
            self.left_menu,
            text=text_buttons[2],
            fg_color="white",
            hover_color=Colors.light_red,
            font=("Montserrat ExtraBold", 15),
            text_color="black",
            corner_radius=15,
            width=200, height=50,
            command=self.list_of_functions[2]
        )
        self.button_three.place(anchor='center', x=125, y=310)

        # Fourth button
        self.button_four = ctk.CTkButton(
            self.left_menu,
            text=text_buttons[3],
            fg_color="white",
            hover_color=Colors.light_red,
            font=("Montserrat ExtraBold", 15),
            text_color="black",
            corner_radius=15,
            width=200, height=50,
            command=self.list_of_functions[3]
        )
        self.button_four.place(anchor='center', x=125, y=365)

        # Exit Button
        self.exit_button = ctk.CTkButton(
            self.left_menu,
            text="Exit",
            fg_color=Colors.gray_0,
            hover_color=Colors.magnum_red,
            font=("Montserrat ExtraBold", 15),
            text_color="white",
            corner_radius=15,
            command=self.exit_menu,
            width=200, height=50
        )
        self.exit_button.place(anchor='center', x=125, y=630)

    def exit_menu(self) -> None:
        """
        :return: The exit button will display a pop-up asking you if you want to close the application or if you want to
         disconnect from the account.
        """

        # We call the pop_up and we set it
        ExitPopUp(self.root)


class ExitPopUp:
    def __init__(self, root: ctk.windows.ctk_tk.CTk) -> None:
        """
        :param root: Need to be the Main Root
        """
        show_the_call(ExitPopUp)

        # Main Root
        self.root = root

        # ExitPopUp Root
        self.exit_pop_up_root = ctk.CTk()

        # ExitPopUp Root Adjustements
        self.exit_pop_up_root._set_appearance_mode("Light")  # We set the theme of the application
        self.exit_pop_up_root.lift()  # We bring the window to the foreground
        self.exit_pop_up_root.resizable(False, False)  # It does not allow the window to be resized
        self.exit_pop_up_root.title('Magnum OPUS')  # Title
        self.exit_pop_up_root.geometry(f"{400}x{200}+{(self.exit_pop_up_root.winfo_screenwidth() - 400) // 2}+"
                             f"{(self.exit_pop_up_root.winfo_screenheight() - 500) // 2 - 50}")  # We set the root size
        self.exit_pop_up_root.protocol("WM_DELETE_WINDOW", self.custom_close)  # We put our own method to close

        # Sets the icon for the window
        self.exit_pop_up_root.iconbitmap('images/ICO/icon logo.ico')

        # Widgets
        self.widgets()

        # Pop-up mainloop
        self.exit_pop_up_root.mainloop()

    def widgets(self) -> None:
        # Main frame
        self.frame = ctk.CTkFrame(
            self.exit_pop_up_root,
            fg_color=Colors.windows_light,
            corner_radius=0
        )
        self.frame.pack(fill='both', expand=True)

        # Background color for title message
        self.info_frame = ctk.CTkFrame(
            self.frame,
            fg_color=Colors.magnum_red,
            corner_radius=30,
            width=150,
            height=40
        )
        self.info_frame.place(anchor='n', x=200, y=10)

        # Title message
        self.info_label = ctk.CTkLabel(
            self.info_frame,
            text='Ce vrei sa faci?',
            font=("INTER BOLD", 18),
            text_color=Colors.windows_light
        )
        self.info_label.pack(anchor='center', padx=10, pady=5)

        # Label that contains all the information we want to display to the user
        self.text_label = ctk.CTkLabel(
            self.frame,
            font=('INTER Medium', 16),
            justify='center',
            text_color='black',
            text='Închizi aplicația?\nSau\nVrei sa te deconectezi?'
        )
        self.text_label.place(anchor='center', x=200, y=100)

        # Frame that contains the buttons
        self.button_frame = ctk.CTkFrame(
            self.exit_pop_up_root,
            width=400,
            height=50,
            fg_color=Colors.gray_0,
            corner_radius=0
        )
        self.button_frame.place(anchor='center', x=200, y=175)

        # First button
        self.button_one = ctk.CTkButton(
            self.button_frame,
            text='Deconectare',
            font=("Montserrat ExtraBold", 14),
            width=100,
            height=30,
            fg_color=Colors.gray_2,
            corner_radius=15,
            hover_color=Colors.magnum_red,
            command=self.back_to_login
        )
        self.button_one.place(anchor='center', x=100, y=25)

        # Second button
        self.button_two = ctk.CTkButton(
            self.button_frame,
            text='Închide aplicația',
            font=("Montserrat ExtraBold", 14),
            width=100,
            height=30,
            fg_color=Colors.gray_2,
            corner_radius=15,
            hover_color=Colors.magnum_red,
            command=self.close_app
        )
        self.button_two.place(anchor='center', x=300, y=25)

    def back_to_login(self) -> None:
        """
        :return: Destroy all the menu items and call the login again
        """

        # We import here Login to avoid cyclic import
        from main import Login

        # We destroy all widgets that main root has
        for widget in self.root.winfo_children():
            widget.destroy()

        # Call the Login
        Login(self.root)

        # Close ExitPopUp
        self.custom_close()

    def close_app(self) -> None:
        """
        :return: Close the entire application
        """
        # Destroy Main Root
        self.root.destroy()

        # Close Exit Pop-Up
        self.custom_close()

    def custom_close(self) -> None:
        """
        :return: Close ExitPopUp's mainloop and destroy ExitPopUp's root
        """
        # We close mainloop
        self.exit_pop_up_root.quit()

        # Destroy the root
        self.exit_pop_up_root.destroy()

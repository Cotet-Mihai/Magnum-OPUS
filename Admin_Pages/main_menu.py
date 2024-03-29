import customtkinter as ctk
from typing import Callable
from basic_functions import show_the_call
from basic_classes import LeftMenu


class MainMenu:
    def __init__(self, root: ctk.windows.ctk_tk.CTk) -> None:
        show_the_call(MainMenu)

        # Root Adjustements
        self.root = root

        # Change the size to root main and center it in the middle of the screen
        self.root.geometry("1200x700+{}+{}".format((self.root.winfo_screenwidth() - 1200) // 2, (
                    self.root.winfo_screenheight() - 700) // 2 - 50))

        # Elements for LeftMenu
        self.text_buttons_left_menu: list[str] = ['1', '2', '3', '4']
        self.functions_for_left_menu: list[Callable] = [lambda: print('Button 1 was press'),
                                                        lambda: print('Button 2 was press'),
                                                        lambda: print('Button 3 was press'),
                                                        lambda: print('Button 4 was press')]

        LeftMenu(self.root, self.text_buttons_left_menu, self.functions_for_left_menu)

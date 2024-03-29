import customtkinter as ctk
from basic_functions import show_the_call


class Personal:
    def __init__(self, root: ctk.windows.ctk_tk.CTk) -> None:
        show_the_call(Personal)

        # Root
        self.root = root

    def widgets(self) -> None:

        self.top_frame = ctk.CTkFrame(
            self.root,
            width=905, height=50
        )

import customtkinter as ctk
from PIL import Image

class Images:
    @staticmethod
    def convert_to_ctk(path, width, height):
        img = Image.open(path)
        image = ctk.CTkImage(
            light_image=img, dark_image=img,
            size=(width ,height)
        )

        return image

    white_logo = convert_to_ctk('images/PNG/white_magnum.png', 100, 58.88)
    red_logo = convert_to_ctk('images/PNG/red_magnum.png', 150, 150)
    user_login = convert_to_ctk('images/PNG/user_login.png', 40, 40)
    password_login = convert_to_ctk('images/PNG/password_login.png', 40, 40)
    seach = convert_to_ctk('images/PNG/search.png', 30, 30)
    calendar = convert_to_ctk('images/PNG/calendar.png', 40, 40)
    slot = convert_to_ctk('images/PNG/slot.png', 50, 50)
    done = convert_to_ctk('images/PNG/done.png', 15, 15)
    undone = convert_to_ctk('images/PNG/undone.png', 15, 15)
    danger = convert_to_ctk('images/PNG/danger.png', 15, 15)
    minus = convert_to_ctk('images/PNG/minus.png', 15, 15)
    equal = convert_to_ctk('images/PNG/equal.png', 15, 15)
    more_than = convert_to_ctk('images/PNG/more_than.png', 35, 35)
    less_than = convert_to_ctk('images/PNG/less_than.png', 35, 35)
    more_than_white = convert_to_ctk('images/PNG/more_than_white.png', 30, 30)
    less_than_white = convert_to_ctk('images/PNG/less_than_white.png', 30, 30)



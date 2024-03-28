import customtkinter as ctk
from basic_functions import show_the_call
from colors import Colors
from images.PNG.png import Images


class Login:
    def __init__(self, root: ctk.windows.ctk_tk.CTk) -> None:
        show_the_call(Login.__name__)

        # Root Adj
        self.root = root
        # Change the size of the root and make it appear in the center of the screen
        self.root.geometry(
            "400x600+{}+{}".format(
                (self.root.winfo_screenwidth() - 400) // 2,
                (self.root.winfo_screenheight() - 500) // 2 - 50
            )
        )

        # Widgets
        self.widgets()

    def widgets(self) -> None:
        self.frame = ctk.CTkFrame(
            self.root,
            width=400, height=600,
            fg_color='white',
            corner_radius=0
        )
        self.frame.place(x=0, y=0)

        self.red_dot = ctk.CTkFrame(
            self.frame,
            width=400, height=400,
            corner_radius=400,
            fg_color=Colors.magnum_red
        )
        self.red_dot.place(anchor='center', x=200, y=0)

        self.logo = ctk.CTkLabel(
            self.red_dot,
            text='',
            image=Images.white_logo
        )
        self.logo.place(anchor='center', x=200, y=260)

        self.text = ctk.CTkLabel(
            self.red_dot,
            text_color='white',
            text='MAGNUM',
            font=('montserrat extrabold', 40)
        )
        self.text.place(anchor='center', x=200, y=330)

        self.username_img = ctk.CTkLabel(
            self.frame,
            text='',
            image=Images.user_login
        )
        self.username_img.place(anchor='center', x=200, y=255)

        self.username = ctk.CTkEntry(
            self.frame,
            font=('montserrat regular', 15),
            text_color=Colors.gray_0,
            width=250, height=40,
            placeholder_text="Utilizator",
            placeholder_text_color=Colors.magnum_red,
            fg_color='white',
            corner_radius=30,
            border_color=Colors.magnum_red,
            justify='center'
        )
        self.username.place(anchor='center', x=200, y=300)

        self.password_img = ctk.CTkLabel(
            self.frame,
            text='',
            image=Images.password_login
        )
        self.password_img.place(anchor='center', x=200, y=355)

        self.password = ctk.CTkEntry(
            self.frame,
            font=('montserrat regular', 15),
            text_color=Colors.gray_0,
            width=250, height=40,
            placeholder_text="Parola", show="*",
            placeholder_text_color=Colors.magnum_red,
            fg_color='white',
            corner_radius=30,
            border_color=Colors.magnum_red,
            justify='center'

        )
        self.password.place(anchor='center', x=200, y=400)
        self.password.bind('<Return>', self.invoke_login_button)

        self.errorLabel = ctk.CTkLabel(
            self.frame,
            font=("Montserrat ExtraBold", 15),
            text="Autentificare eșuată",
            text_color="#cf0a0a"
        )

        self.buttons_frame = ctk.CTkFrame(
            self.frame,
            width=400, height=60,
            fg_color=Colors.gray_0,
            corner_radius=0
        )
        self.buttons_frame.place(anchor='s', x=200, y=600)

        self.login_button = ctk.CTkButton(
            self.buttons_frame,
            width=200, height=60,
            text='Conectează-te',
            font=('montserrat extrabold', 15),
            corner_radius=0,
            fg_color=Colors.gray_0,
            hover_color=Colors.green_1,
            command=self.verify_authentification
        )
        self.login_button.place(anchor='center', x=100, y=30)

        self.close_button = ctk.CTkButton(
            self.buttons_frame,
            width=200, height=60,
            text='Închide',
            font=('montserrat extrabold', 15),
            corner_radius=0,
            fg_color=Colors.gray_0,
            hover_color=Colors.magnum_red,
            command=self.close_app
        )
        self.close_button.place(anchor='center', x=300, y=30)

    def verify_authentification(self) -> None:

        # We extract the authentication data and store them as variables
        username = self.username.get()
        password = self.password.get()

        # Connexion DataBase
        conn = SQL_Server.connStr
        my_cursor = conn.cursor()

        # Use parameters to avoid SQL injection
        query = 'SELECT * FROM Users WHERE Username=? And Password=?'
        search = my_cursor.execute(query, (username, password))

        # Get information from selected row
        result = search.fetchone()

        # If result it s not Null
        if result:
            # Set MyProfile
            MyProfile.my_Profile = MyProfile(username, password, result[2], result[1], result[5], result[-1], result[6], result[0])
            role = result[-1]

            # Select Main_Menu by Role
            match role:
                case 'Admin':
                    pass
                case 'Manager':
                    pass
                case 'Casier':
                    print('Type Account: Casier')
                    self.go_to_menu(Main_menu)

        # Else show error label
        else:
            self.errorLabel.place(anchor='center', x=200, y=480)
            print("Autentificare eșuată.")
    def invoke_login_button(self, event=None) -> None:
        self.login_button.invoke()
    def go_to_menu(self, page) -> None:
        self.frame.destroy()
        page(self.root)
    def close_app(self) -> None:
        self.root.quit()

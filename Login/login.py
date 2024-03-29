import customtkinter as ctk
from basic_functions import show_the_call
from colors import Colors
from images.PNG.png import Images
from database import SqlServer, MyProfile, SqlAccounts
from Admin_Pages.main_menu import MainMenu as AdminMainMenu


class Login:
    def __init__(self, root: ctk.windows.ctk_tk.CTk) -> None:

        show_the_call(Login)

        # Root Adjustments
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
        # Frame that contains all login widgets
        self.frame = ctk.CTkFrame(
            self.root,
            width=400, height=600,
            fg_color='white',
            corner_radius=0
        )
        self.frame.place(x=0, y=0)

        # Style element
        self.red_dot = ctk.CTkFrame(
            self.frame,
            width=400, height=400,
            corner_radius=400,
            fg_color=Colors.magnum_red
        )
        self.red_dot.place(anchor='center', x=200, y=0)

        # Logo PNG
        self.logo = ctk.CTkLabel(
            self.red_dot,
            text='',
            image=Images.white_logo
        )
        self.logo.place(anchor='center', x=200, y=260)

        # Brand Name
        self.text = ctk.CTkLabel(
            self.red_dot,
            text_color='white',
            text='MAGNUM',
            font=('montserrat extrabold', 40)
        )
        self.text.place(anchor='center', x=200, y=330)

        # Username PNG
        self.username_img = ctk.CTkLabel(
            self.frame,
            text='',
            image=Images.user_login
        )
        self.username_img.place(anchor='center', x=200, y=255)

        # Username Entry
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

        # Password PNG
        self.password_img = ctk.CTkLabel(
            self.frame,
            text='',
            image=Images.password_login
        )
        self.password_img.place(anchor='center', x=200, y=355)

        # Password Entry
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
        self.password.bind('<Return>', self.invoke_login_button)  # When you press enter, the login button is pressed

        # Error Label
        self.errorLabel = ctk.CTkLabel(
            self.frame,
            font=("Montserrat ExtraBold", 15),
            text="Autentificare eșuată",
            text_color="#cf0a0a"
        )

        # Frame that contains the buttons
        self.buttons_frame = ctk.CTkFrame(
            self.frame,
            width=400, height=60,
            fg_color=Colors.gray_0,
            corner_radius=0
        )
        self.buttons_frame.place(anchor='s', x=200, y=600)

        # Login Button
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

        # Close Button
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
        """
        :return: If it matches, go to the main menu (depending on the role type),
            if it doesn't match, display the Error Label
        Execute the query of the database if there is a user with the entered name and password.
        """

        # We extract the authentication data and store them as variables
        username = self.username.get()
        password = self.password.get()

        try:
            # Connection to Guest DataBase
            self.guest_database = SqlServer('Guest', SqlAccounts.guest)
            self.guest_conn = self.guest_database.get_connStr()
            self.guest_cursor = self.guest_conn.cursor()

            # Use parameters to avoid SQL injection
            all_users_query = 'SELECT * FROM Guest.dbo.Users WHERE Username=? And Password=?'
            all_users_search = self.guest_cursor.execute(all_users_query, (username, password))

            # Get information from selected row
            result = all_users_search.fetchone()

            # If result it s not None
            if result is not None:

                # Save information in a dictionary:
                logged_user: dict = {'ID': result[0],
                                     'Username': result[1],
                                     'Password': result[2],
                                     'Role': result[3]
                                     }
                # Match Role with level access
                match logged_user['Role']:

                    # CASE ADMIN
                    case 'Admin':
                        print('Type Account: Admin')

                        # Query to get the admin account
                        all_admin_query = ('SELECT * FROM Guest.dbo.Admin_Accounts WHERE ID=? And User_Name=?'
                                           ' AND Password=?')
                        all_admin_search = self.guest_cursor.execute(all_admin_query,
                                                                     (logged_user['ID'], logged_user['Username'],
                                                                      logged_user['Password']))
                        user = all_admin_search.fetchone()

                        # After we get all the infromations we need from Database we close the connection
                        self.guest_conn.close()

                        # Save all infromations in a dictionary
                        user_found: dict = {'ID': user[0],
                                            'Last_Name': user[1],
                                            'First_Name': user[2],
                                            'Username': user[3],
                                            'Password': user[4],
                                            'Age': user[5],
                                            'Sex': user[6],
                                            'Salary': user[7],
                                            'Phone_Number': user[8],
                                            'Email': user[9]}

                        # Set my_profile with dictonary result
                        MyProfile.my_Profile = MyProfile(user_found['ID'], user_found['Last_Name'],
                                                         user_found['First_Name'], user_found['Username'],
                                                         user_found['Password'], user_found['Age'], user_found['Sex'],
                                                         user_found['Salary'], user_found['Phone_Number'],
                                                         user_found['Email'], 'Admin'
                                                         )
                        self.go_to_menu(AdminMainMenu)

                    # CASE MANAGER
                    case 'Manager':
                        print('Type Account: Manager')

                    # CASE Cashier
                    case 'Cashier':
                        print('Type Account: Cashier')

            # If result is None
            else:
                self.errorLabel.place(anchor='center', x=200, y=480)
                print("Autentificare eșuată.")

        except Exception as e:
            print(e)

    def invoke_login_button(self, event=None) -> None:
        self.login_button.invoke()

    def go_to_menu(self, page) -> None:
        self.frame.destroy()
        page(self.root)

    def close_app(self) -> None:
        self.root.quit()

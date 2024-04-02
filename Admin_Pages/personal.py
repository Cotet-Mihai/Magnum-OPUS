import customtkinter as ctk
from basic_functions import show_the_call
from colors import Colors
from database import SqlServer, SqlAccounts


class Personal:
    def __init__(self, root: ctk.windows.ctk_tk.CTk) -> None:
        show_the_call(Personal)

        # Root
        self.root = root

        # Widgets
        self.widgets()

        # Directly invoke the add_person button to be the first page displayed
        self.add_location.invoke()

    def widgets(self) -> None:
        """
        :return: Add buttons widgets
        """
        # Top Frame
        self.top_frame = ctk.CTkFrame(
            self.root,
            corner_radius=0,
            width=905, height=100,
            fg_color=Colors.gray_0
        )
        self.top_frame.place(x=0, y=0)

        # Title
        self.title_label = ctk.CTkLabel(
            self.top_frame,
            text="PERSONAL",
            text_color="white",
            font=("Montserrat ExtraBold", 70)
        )
        self.title_label.place(x=15, y=0)

        # BUTTONS FRAME 1.0
        self.buttons_frame = ctk.CTkFrame(
            self.root,
            width=905, height=50,
            corner_radius=15
        )
        self.buttons_frame.place(x=0, y=115)

        # Add person button 1.1
        self.add_person = ctk.CTkButton(
            self.buttons_frame,
            width=40, height=40,
            corner_radius=15,
            text='P',
            command=self.add_person_button_widgets
        )
        self.add_person.place(x=50, y=5)

        # Add new location 1.2
        self.add_location = ctk.CTkButton(
            self.buttons_frame,
            width=40, height=40,
            corner_radius=15,
            text='L',
            command=self.add_location_button_widgets
        )
        self.add_location.place(x=5, y=5)

        # MAIN FRAMES 2.0
        # Add new person 2.1
        self.main_add_person = ctk.CTkFrame(
            self.root,
            width=905, height=490,
            corner_radius=15
        )

        # Add new location 2.2
        self.main_add_location = ctk.CTkFrame(
            self.root,
            width=905, height=490,
            corner_radius=15
        )

    def add_location_button_widgets(self) -> None:

        # Hide the other pages
        self.main_add_person.place_forget()

        # Select type location
        self.type = ctk.CTkSegmentedButton(
            self.main_add_location,
            height=30,
            values=["Cazino", "Agentie", "Partener"],
            command=self.select_type_location
        )
        self.type.place(x=15, y=15)

        self.main_add_location.place(x=0, y=180)

    """def select_type_location(self, value: str) -> None:

        match value:
            case 'Cazino':
                print('Type: Casino')

                def add_to_tabel():

                    # Get all the information in vars
                    casino_id = self.casino_id.get()
                    alias = self.casino_alias.get()
                    country = self.casino_country.get()
                    city = self.casino_city.get()
                    address = self.casino_address.get()

                    try:
                        # Connect to database
                        add_casino_server = SqlServer('Locations', SqlAccounts.admin)
                        add_casino_con = add_casino_server.connStr
                        add_casino_cursor = add_casino_con.cursor()

                        # Add the information in the sql table
                        add_a_new_casino = ("INSERT INTO Casinos (id, alias, country, city, address)"
                                            " VALUES (?, ?, ?, ?, ?)")
                        # The values we save
                        add_casino_values = (casino_id, alias, country, city, address)
                        # Execute command
                        add_casino_cursor.execute(add_a_new_casino, add_casino_values)
                        # Commit the addition
                        add_casino_con.commit()
                        # Close connection to DataBase
                        add_casino_con.close()

                        print('Successfully saved!')

                    except Exception as e:
                        print(e)
                        print('An error occurred during the save.')

                # Main Frame
                self.casino_tab = ctk.CTkFrame(
                    self.main_add_location,
                    width=500, height=400,
                    corner_radius=15
                )
                self.casino_tab.place(x=15, y=15)

                # Title
                self.casino_title = ctk.CTkLabel(
                    self.casino_tab,
                    text='ADAUGĂ UN NOU CAZINO',
                    font=('INTER BOLD', 20)
                )
                self.casino_title.place(anchor='center', x=250, y=30)

                # ID
                self.casino_id = ctk.CTkEntry(
                    self.casino_tab,
                    placeholder_text='ID'
                )
                self.casino_id.place(anchor='center', x=250, y=80)

                # Alias
                self.casino_alias = ctk.CTkEntry(
                    self.casino_tab,
                    placeholder_text='Alias'
                )
                self.casino_alias.place(anchor='center', x=250, y=110)

                # Country
                self.casino_country = ctk.CTkEntry(
                    self.casino_tab,
                    placeholder_text='Judet'
                )
                self.casino_country.place(anchor='center', x=250, y=140)

                # City
                self.casino_city = ctk.CTkEntry(
                    self.casino_tab,
                    placeholder_text='Localitate'
                )
                self.casino_city.place(anchor='center', x=250, y=170)

                # Address
                self.casino_address = ctk.CTkEntry(
                    self.casino_tab,
                    placeholder_text='Adresa',
                    width=140, height=100
                )
                self.casino_address.place(anchor='center', x=250, y=236)

                # Add Button

                self.add_location_button = ctk.CTkButton(
                    self.casino_tab,
                    text='Adauga',
                    command=add_to_tabel
                )
                self.add_location_button.place(anchor='center', x=250, y=350)

            case 'Agentie':
                print('Type: Agency')

                def add_to_tabel():

                    # Get all the information in vars
                    agency_id = self.agency_id.get()
                    alias = self.agency_alias.get()
                    country = self.agency_country.get()
                    city = self.agency_city.get()
                    address = self.agency_address.get()

                    try:
                        # Connect to database
                        add_agency_server = SqlServer('Locations', SqlAccounts.admin)
                        add_agency_con = add_agency_server.connStr
                        add_agency_cursor = add_agency_con.cursor()

                        # Add the information in the sql table
                        add_a_new_agency = ("INSERT INTO Agencies (id, alias, country, city, address)"
                                            " VALUES (?, ?, ?, ?, ?)")
                        # The values we save
                        add_agency_values = (agency_id, alias, country, city, address)
                        # Execute command
                        add_agency_cursor.execute(add_a_new_agency, add_agency_values)
                        # Commit the addition
                        add_agency_con.commit()
                        # Close connection to DataBase
                        add_agency_con.close()

                        print('Successfully saved!')

                    except Exception as e:
                        print(e)
                        print('An error occurred during the save.')

                # Main Frame
                self.agency_tab = ctk.CTkFrame(
                    self.main_add_location,
                    width=500, height=400,
                    corner_radius=15
                )
                self.agency_tab.place(x=15, y=15)

                # Title
                self.title = ctk.CTkLabel(
                    self.agency_tab,
                    text='ADAUGĂ O NOUĂ AGENȚIE',
                    font=('INTER BOLD', 20)
                )
                self.title.place(anchor='center', x=250, y=30)

                # ID
                self.agency_id = ctk.CTkEntry(
                    self.agency_tab,
                    placeholder_text='ID'
                )
                self.agency_id.place(anchor='center', x=250, y=80)

                # Alias
                self.agency_alias = ctk.CTkEntry(
                    self.agency_tab,
                    placeholder_text='Alias'
                )
                self.agency_alias.place(anchor='center', x=250, y=110)

                # Country
                self.agency_country = ctk.CTkEntry(
                    self.agency_tab,
                    placeholder_text='Județ'
                )
                self.agency_country.place(anchor='center', x=250, y=140)

                # City
                self.agency_city = ctk.CTkEntry(
                    self.agency_tab,
                    placeholder_text='Localitate'
                )
                self.agency_city.place(anchor='center', x=250, y=170)

                # Address
                self.agency_address = ctk.CTkEntry(
                    self.agency_tab,
                    placeholder_text='Adresă',
                    width=140, height=100
                )
                self.agency_address.place(anchor='center', x=250, y=236)

                # Add Button
                self.add_location_button = ctk.CTkButton(
                    self.agency_tab,
                    text='Adaugă',
                    command=add_to_tabel
                )
                self.add_location_button.place(anchor='center', x=250, y=350)

                # Main Frame
                self.agency_tab = ctk.CTkFrame(
                    self.main_add_location,
                    width=505, height=400,
                    corner_radius=15,
                    fg_color='yellow'
                )
                self.agency_tab.place(x=15, y=60)

            case 'Partener':
                print('Type: Partnership')

                def add_to_tabel():
                    # Get all the information in vars
                    partner_id = self.partnership_id.get()
                    alias = self.partnership_alias.get()
                    country = self.partnership_country.get()
                    city = self.partnership_city.get()
                    address = self.partnership_address.get()

                    try:
                        # Connect to database
                        add_partner_server = SqlServer('Locations', SqlAccounts.admin)
                        add_partner_con = add_partner_server.connStr
                        add_partner_cursor = add_partner_con.cursor()

                        # Add the information in the sql table
                        add_a_new_partner = ("INSERT INTO Partnerships (id, alias, country, city, address)"
                                             " VALUES (?, ?, ?, ?, ?)")
                        # The values we save
                        add_partner_values = (partner_id, alias, country, city, address)
                        # Execute command
                        add_partner_cursor.execute(add_a_new_partner, add_partner_values)
                        # Commit the addition
                        add_partner_con.commit()
                        # Close connection to DataBase
                        add_partner_con.close()

                        print('Successfully saved!')

                    except Exception as e:
                        print(e)
                        print('An error occurred during the save.')

                # Main Frame
                self.partnership_tab = ctk.CTkFrame(
                    self.main_add_location,
                    width=500, height=400,
                    corner_radius=15
                )
                self.partnership_tab.place(x=15, y=15)

                # Title
                self.title = ctk.CTkLabel(
                    self.partnership_tab,
                    text='ADAUGĂ UN NOU PARTENERIAT',
                    font=('INTER BOLD', 20)
                )
                self.title.place(anchor='center', x=250, y=30)

                # ID
                self.partnership_id = ctk.CTkEntry(
                    self.partnership_tab,
                    placeholder_text='ID'
                )
                self.partnership_id.place(anchor='center', x=250, y=80)

                # Alias
                self.partnership_alias = ctk.CTkEntry(
                    self.partnership_tab,
                    placeholder_text='Alias'
                )
                self.partnership_alias.place(anchor='center', x=250, y=110)

                # Country
                self.partnership_country = ctk.CTkEntry(
                    self.partnership_tab,
                    placeholder_text='Județ'
                )
                self.partnership_country.place(anchor='center', x=250, y=140)

                # City
                self.partnership_city = ctk.CTkEntry(
                    self.partnership_tab,
                    placeholder_text='Localitate'
                )
                self.partnership_city.place(anchor='center', x=250, y=170)

                # Address
                self.partnership_address = ctk.CTkEntry(
                    self.partnership_tab,
                    placeholder_text='Adresa',
                    width=140, height=100
                )
                self.partnership_address.place(anchor='center', x=250, y=236)

                # Add Button
                self.add_location_button = ctk.CTkButton(
                    self.partnership_tab,
                    text='Adauga',
                    command=add_to_tabel
                )
                self.add_location_button.place(anchor='center', x=250, y=350)"""
    def select_type_location(self, value) -> None:
        match value:
            case 'Cazino':
                add_location(self.main_add_location, 'Adauga un nou cazino', 'Casinos')
            case 'Agentie':
                add_location(self.main_add_location, 'Adauga o noua Agentie', 'Agencies')
            case 'Partener':
                add_location(self.main_add_location, 'Adauga un nou Partener', 'Partnerships')

    def add_person_button_widgets(self) -> None:

        # Hide the other pages
        self.main_add_location.place_forget()

        # Select type account
        self.type = ctk.CTkSegmentedButton(
            self.main_add_person,
            height=30,
            values=["Manager", "Casier"],
            command=self.select_role_person
        )
        self.type.place(x=15, y=15)

        self.main_add_person.place(x=0, y=180)

    def select_role_person(self, value: str) -> None:

        match value:
            case 'Manager':
                print('Selected Type: Manager')

                self.manager_tab = ctk.CTkFrame(
                    self.main_add_person,
                    width=505, height=400,
                    corner_radius=15,
                    fg_color='red'
                )
                self.manager_tab.place(x=15, y=60)

            case 'Casier':
                print('Selected Type: Casier')

                self.casier_tab = ctk.CTkFrame(
                    self.main_add_person,
                    width=505, height=400,
                    corner_radius=15,
                    fg_color='yellow'
                )
                self.casier_tab.place(x=15, y=60)


class add_location:
    def __init__(self, root , title_text: str, tabel_name: str):
        # Root
        self.root = root

        # Vars
        self.title_text = title_text
        self.table_name = tabel_name

        # Widgets
        self.widgets()

    def widgets(self) -> None:
        # Main Frame
        self.location_tab = ctk.CTkFrame(
            self.root,
            width=500, height=400,
            corner_radius=15
        )
        self.location_tab.place(x=15, y=60)

        # Title
        self.title = ctk.CTkLabel(
            self.location_tab,
            text=self.title_text,
            font=('INTER BOLD', 20)
        )
        self.title.place(anchor='center', x=250, y=30)

        # ID
        self.location_id = ctk.CTkEntry(
            self.location_tab,
            placeholder_text="ID"
        )
        self.location_id.place(anchor='center', x=250, y=80)

        # Alias
        self.location_alias = ctk.CTkEntry(
            self.location_tab,
            placeholder_text="Alias"
        )
        self.location_alias.place(anchor='center', x=250, y=110)

        # Country
        self.location_country = ctk.CTkEntry(
            self.location_tab,
            placeholder_text='Localitate'
        )
        self.location_country.place(anchor='center', x=250, y=140)

        # City
        self.location_city = ctk.CTkEntry(
            self.location_tab,
            placeholder_text='Judetul'
        )
        self.location_city.place(anchor='center', x=250, y=170)

        # Address
        self.location_address = ctk.CTkEntry(
            self.location_tab,
            placeholder_text='Adresa',
            width=140, height=100
        )
        self.location_address.place(anchor='center', x=250, y=236)

        # Add Button
        self.add_location_button = ctk.CTkButton(
            self.location_tab,
            text='Adaugă',
            command=self.add_location_to_database
        )
        self.add_location_button.place(anchor='center', x=250, y=350)

    def get_values(self) -> tuple:

        # Get all information and save them to vars
        id_location: str = self.location_id.get()
        alias: str = self.location_alias.get()
        city: str = self.location_city.get()
        country: str = self.location_country.get()
        address: str = self.location_address.get()

        # Stock all vars in a tuplu
        all_informations: tuple = (id_location, alias, city, country, address)

        # Return tuplu
        return all_informations

    def add_location_to_database(self) -> None:
        try:
            # Connect to database
            add_location_server = SqlServer('Locations', SqlAccounts.admin)
            add_location_con = add_location_server.connStr
            add_location_cursor = add_location_con.cursor()

            # Add the information in the sql table
            add_location_query = f"INSERT INTO {self.table_name} (id, alias, country, city, address) VALUES (?, ?, ?, ?, ?)"
            # Get values
            values = self.get_values()
            # Execute command
            add_location_cursor.execute(add_location_query, values)
            # Commit the addition
            add_location_con.commit()
            # Close connection to DataBase
            add_location_con.close()

            print('Successfully saved!')

        except Exception as e:
            print(e)
            print('An error occurred during the save.')





if __name__ == '__main__':
    # TEST

    # Root
    root = ctk.CTk()
    # Size Root
    root.geometry('905x670')
    # Not resizable
    root.resizable(False, False)
    # Call Personal
    Personal(root)
    # Mainloop
    root.mainloop()

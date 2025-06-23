import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._btnCreaGrafo = None
        self._txtInNcanzoni = None
        self._btnAnalisiComp = None
        self.ddAlbum2 = None
        self.ddAlbum2Value = None
        self._txtInSoglia = None
        self.ddAlbum1 = None
        self.ddAlbum1Value = None
        self._page = page
        self._page.title = "TdP - Esame del 14/09/2022"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP - Esame del 14/09/2022", color="red", size=24)
        self._page.controls.append(self._title)

        #ROW1
        self._txtInNcanzoni = ft.TextField(label="# canzoni")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(self._txtInNcanzoni, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW2
        self.ddAlbum1 = ft.Dropdown(label="Album", on_change = self.on_ddAlbum1_change)
        self._btnAnalisiComp = ft.ElevatedButton(text = "Analisi Componente.",
                                                 on_click=self._controller.handleStampaAdiacenze)

        row2 = ft.Row([
            ft.Container(self.ddAlbum1, width=300),
            ft.Container(self._btnAnalisiComp, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #ROW3
        self.ddAlbum2 = ft.Dropdown(label="Album", on_change = self.on_ddAlbum2_change)
        self.btnCalcolaPercorso = ft.ElevatedButton(text="Calcola Percorso",
                                                    on_click=self._controller.handleCalcolaPercorso)
        row3 = ft.Row([
            ft.Container(self.ddAlbum2, width=300),
            ft.Container(self.btnCalcolaPercorso, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        
        #ROW4
        self._txtInSoglia = ft.TextField(label="Soglia")                                 
        row4 = ft.Row([
            ft.Container(self._txtInSoglia, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)
        

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def on_ddAlbum1_change(self, e):
        self.ddAlbum1Value = self.ddAlbum1.value
        self.update_page()

    def on_ddAlbum2_change(self, e):
        self.ddAlbum2Value = self.ddAlbum2.value
        self.update_page()

    def update_page(self):
        self._page.update()

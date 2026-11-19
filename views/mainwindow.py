from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import *
from  components.sidebar import SideBar


class MainWindow(Window):
    sidebar = SideBar()

    def __init__(self):
        super().__init__()
        self.create_ui()

    def create_ui(self):
        ...

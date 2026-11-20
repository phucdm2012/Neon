from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import *
from  components.sidebar import SideBar


class MainWindow(Window):

    def __init__(self):
        super().__init__()
        self.create_ui()
        self.sidebar = SideBar()

    def create_ui(self):
        ...

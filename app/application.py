from win32more.winui3 import XamlApplication
from views.mainwindow import  MainWindow


class Application(XamlApplication):
    def __init__(self):
        super().__init__()
        self.window: MainWindow

    def OnLaunched(self, args):
        self.window = MainWindow()
        self.window.Activate()

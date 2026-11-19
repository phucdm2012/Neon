from win32more.Microsoft.UI.Xaml.Controls import *


class SideBar:
    def __init__(self):
        self.widget = StackPanel()

        self.dictionary_page_button = Button("Dictionary Page")

        self.widget.Children.Append(self.dictionary_page_button)

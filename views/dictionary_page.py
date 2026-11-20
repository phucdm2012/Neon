from win32more.Microsoft.UI.Xaml import CornerRadius, Thickness
from win32more.Microsoft.UI.Xaml.Controls import  *
from win32more.Windows.UI import Color


class DictionaryPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._setup_scroll_view()
        self._setup_content_view()
        self._setup_utility_bar()
        self._setup_root_view()

    def _setup_scroll_view(self):
        self.scroll_view = ScrollView()

        self.scroll_view.VerticalScrollBarVisibility = ScrollBarVisibility.Auto
        self.scroll_view.ZoomChainMode = ZoomMode.Enabled

    def _setup_content_view(self):
        self.content_view = Panel()
        self.content_view.Background = Color.Transparent

        self.scroll_view.Content = self.content_view

    def _setup_utility_bar(self):
        self.utility_bar = Border()

        self.utility_bar.CornerRadius = CornerRadius(8, 8, 8, 8)
        self.utility_bar.Padding = Thickness(16, 16, 16, 16)

    def _setup_root_view(self):
        self.root_view = Grid()
        self.root_view.Children.Append(self.scroll_view)
        self.root_view.Children.Append(self.utility_bar)

        self.Content = self.root_view

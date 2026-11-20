from win32more.Microsoft.UI.Xaml.Controls import  *
from win32more.Windows.UI import Color


class DictionaryPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._setup_scroll_view()
        self._setup_content_view()

    def _setup_scroll_view(self):
        self.scroll_view = ScrollView()

        self.scroll_view.VerticalScrollBarVisibility = ScrollBarVisibility.Auto
        self.scroll_view.ZoomChainMode = ZoomMode.Enabled

    def _setup_content_view(self):
        self.content_view = Panel()
        self.content_view.Background = Color.Transparent

        self.scroll_view.Content = self.content_view

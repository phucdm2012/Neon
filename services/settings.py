from  pathlib import Path
import ruamel.yaml

CURRENT_DIR = Path(__file__).parent
SETTINGS_DIR = CURRENT_DIR / 'settings'
SETTINGS_DIR.touch(exist_ok=True)

LANGUAGES = open(str(CURRENT_DIR / ''))

UI_CONTENT = {
    'vi': {
        'dictionary_sidebar_button': 'Từ điển',
        'settings_sidebar_button': 'Cài đặt',
    },
    'en': {
        'dictionary_sidebar_button': 'Dictionary Page',
        'settings_sidebar_button': 'Settings',
    },
    'jp': {
        'dictionary_sidebar_button': '辞典',
        'settings_sidebar_button': '改革',
    },
    'zh': {
        'dictionary_sidebar_button': '词典',
        'settings_sidebar_button': '安装',
    },
}

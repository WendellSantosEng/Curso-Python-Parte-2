from pathlib import Path
import sys

# Paths
ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / "files"
WINDOW_ICON_PATH = FILES_DIR / "icon_transparence.png"

# colors

PRIMARY_COLOR = "#d2691e"
DARKER_PRIMARY_COLOR = "#a0522d"
DARKEST_PRIMARY_COLOR = "#8b4513"


# icon config
if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')
        

# size configs        
BIG_FONT_SIZE = 30
MEDIUM_FONT_SIZE = 20
SMALL_FONT_SIZE = 14
TEXT_MARGIN = 10
MINIMUM_WIDTH = 300
from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow, QIcon
from styles import setupTheme
from variables import WINDOW_ICON_PATH

from PySide6.QtWidgets import QApplication, QLabel
import sys

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info

    info = Info("Sua conta")
    window.addWidgetToVLayout(info)

    # display
    display = Display()
    window.addWidgetToVLayout(display)

    # grid
    buttonsGrid = ButtonsGrid(display,info,window)
    window.vLayout.addLayout(buttonsGrid)

    # last thing to do
    window.adjustFixedSize()
    window.show()
    app.exec()



from buttons import *
from display import *
from info import *
from main_window import *
from styles import *
from variables import *
from PySide6.QtWidgets import QApplication, QLabel

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
    buttonsGrid = ButtonsGrid(display,info)
    window.vLayout.addLayout(buttonsGrid)

    # last thing to do
    window.adjustFixedSize()
    window.show()
    app.exec()



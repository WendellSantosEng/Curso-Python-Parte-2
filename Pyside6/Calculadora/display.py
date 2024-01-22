from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN
from PySide6.QtCore import Qt, Signal
from utils import isEmpty, isNumOrDot

class Display(QLineEdit):

    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [ KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [ KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [ KEYS.Key_Escape, KEYS.Key_C]

        if isEnter:
            print("eq")
            self.eqPressed.emit()
            return event.ignore
        if isDelete:
            print("del")
            self.delPressed.emit()
            return event.ignore
        if isEsc:
            print("clear")
            self.clearPressed.emit()
            return event.ignore

        if isEmpty(text):
            return event.ignore

        if isNumOrDot(text):
            print("input")
            self.inputPressed.emit()
            return event.ignore

        # Se quer que digita no display ou não
        return super().keyPressEvent(event)

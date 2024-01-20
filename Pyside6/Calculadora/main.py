import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QLabel

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    window = QMainWindow()
    central_widget = QWidget()
    v_layout = QVBoxLayout()

    central_widget.setLayout(v_layout)
    
    label_1 = QLabel("Meu texto")

    v_layout.addWidget(label_1)

    window.setCentralWidget(central_widget)
    window.show()

    app.exec()

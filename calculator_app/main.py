# Import the modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout


class CalcApp(QWidget):

    def __init__(self):
        super().__init__()
    # App settings
        self.setWindowTitle("Calculator")
        self.resize(250, 300)

    # All objects/widgets
        self.text_box = QLineEdit()
        self.grid = QGridLayout()

        self.buttons = ["7", "8", "9", "/",
                        "4", "5", "6", "*",
                        "1", "2", "3", "-",
                        "0", ".", "=", "+"]

        self.clear = QPushButton("C")
        self.delete = QPushButton("<")

        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        # Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)
        master_layout.addLayout(button_row)

        self.setLayout(master_layout)

    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                self.text_box.setText("Error")

        elif text == "C":
            self.text_box.clear()

        elif text == "<":
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])
        else:
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text)


# Show/RUn
if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.show()
    app.exec_()

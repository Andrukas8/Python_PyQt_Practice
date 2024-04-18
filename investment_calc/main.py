from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTreeView, QLineEdit, QMainWindow, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class FinanceApp(QMainWindow):
    def __init__(self):
        super(FinanceApp, self).__init__()
        self.setWindowTitle("InterestRates 2.0")
        self.resize(800, 600)

        main_window = QWidget()
        self.rate_text = QLabel("Interest Rate (%):")
        self.rate_input = QLineEdit()

        self.initial_text = QLabel("Initial Investment:")
        self.initial_input = QLineEdit()

        self.years_text = QLabel("Years to Invest:")
        self.years_input = QLineEdit()

        # Creation of a TreeView
        self.model = QStandardItemModel()
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)

        # Buttons
        self.calc_button = QPushButton("Calculate")
        self.clear_button = QPushButton("Clear")

        # Figure
        self.figure = QLabel("--- Chart will be here soon ---")

        # Design
        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        # Adding items to row 1
        self.row1.addWidget(self.rate_text)
        self.row1.addWidget(self.rate_input)

        self.row1.addWidget(self.initial_text)
        self.row1.addWidget(self.initial_input)

        self.row1.addWidget(self.years_text)
        self.row1.addWidget(self.years_input)

        # Adding items to row 2
        self.col1.addWidget(self.tree_view)
        self.col1.addWidget(self.calc_button)
        self.col1.addWidget(self.clear_button)

        self.col2.addWidget(self.figure)

        self.row2.addLayout(self.col1, 30)
        self.row2.addLayout(self.col2, 70)

        # Adding row 1 and row 2 to master_layout
        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)

        # Setting layout for the window
        main_window.setLayout(self.master_layout)

        self.setCentralWidget(main_window)

        self.calc_button.clicked.connect(self.calc_interest)
        self.clear_button.clicked.connect(self.reset)

    def calc_interest(self):
        initial_investment = None
        try:
            interest_rate = float(self.rate_input.text())
            initial_investment = float(self.initial_input.text())
            num_years = int(self.years_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Enter a number")
            return

        total = initial_investment
        for year in range(1, num_years+1):
            total += total * (interest_rate/100)
            item_year = QStandardItem(str(year))
            item_total = QStandardItem("{:.2f}".format(total))
            self.model.appendRow([item_year, item_total])

    def reset(self):
        self.rate_input.clear()
        self.initial_input.clear()
        self.years_input.clear()
        self.model.clear()


if __name__ == "__main__":
    app = QApplication([])
    my_app = FinanceApp()
    my_app.show()
    app.exec_()

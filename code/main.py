from PyQt5.QtWidgets import QVBoxLayout, QWidget, QCheckBox, QApplication, QMainWindow
import sys


class Main(QMainWindow):
    """
    Main window for displaying character sheet
    """

    def __init__(self, *args):
        super().__init__(*args)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Stream Checklist")
        self.make_checklist()
        self.setCentralWidget(self.checklist)

    def make_checklist(self):
        self.checklist = QWidget(parent=self)
        layout = QVBoxLayout()

        with open("settings.txt") as f:
            for line in f.readlines():
                button = QCheckBox()
                button.setText(line.strip())
                layout.addWidget(button)

        layout.addStretch()
        self.checklist.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

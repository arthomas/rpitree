import sys
from ledcontrol import LedControl
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QComboBox, QPushButton
import sip
from multiprocessing import Process


class Gui(QWidget):

    def __init__(self):
        super().__init__()
        sip.setapi("QString", 2)
        self.process = False
        self.controlled = LedControl()
        self.ledCombo = QComboBox()
        self.ledCombo.addItem("All")
        j = 1
        for i in range(2, 26):
            self.ledCombo.addItem(str(j))
            j += 1
        self.valueCombo = QComboBox()
        for i in range(0, 11):
            self.valueCombo.addItem(str(i/10))
        self.delayCombo = QComboBox()
        for i in range(0, 11):
            self.delayCombo.addItem(str(i/10))
        self.randomCombo = QComboBox()
        self.randomCombo.addItem("No")
        self.randomCombo.addItem("Yes")
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)
        ledtext = QLabel("LED")
        randomtext = QLabel("Random?")
        delaytext = QLabel("Delay")
        valuetext = QLabel("Value")
        applybutton = QPushButton("Apply")
        applybutton.clicked.connect(self.apply)
        layout.addWidget(randomtext, 0, 0)
        layout.addWidget(ledtext, 1, 0)
        layout.addWidget(delaytext, 2, 0)
        layout.addWidget(valuetext, 3, 0)
        layout.addWidget(self.randomCombo, 0, 1)
        layout.addWidget(self.ledCombo, 1, 1)
        layout.addWidget(self.delayCombo, 2, 1)
        layout.addWidget(self.valueCombo, 3, 1)
        layout.addWidget(applybutton, 4, 1)
        self.setWindowTitle("XMas Tree Control")
        self.setGeometry(300, 300, 500, 200)
        self.show()



    def apply(self):
        led = self.ledCombo.currentText()
        random = self.randomCombo.currentIndex()
        delay = self.delayCombo.currentText()
        value = self.valueCombo.currentText()
        if self.process:
            self.process.terminate()
        self.process = Process(target=self.controlled.ledchange, args=(led, random, delay, value))
        self.process.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())

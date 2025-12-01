from PyQt5.QtWidgets import QApplication, QLabel

class Qt_Gui:
    
    def __init__(self):
        self.app = QApplication([])
        label = QLabel('Hello World!')
        label.show()
        self.app.exec()

#interface()



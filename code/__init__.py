import sys
from code.gui import *

__author__ = "Roman Nabiullin"
__email__ = "r.nabiullin@innopolis.university"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
import sys
from Life.LifeViewer import *
from Life.LifeGenerator import *
from Life.TurtleViewer import *
import time\


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbRun.clicked.connect(self.button_click)
        self.ui.cbOutType.currentIndexChanged.connect(self.visualization_type_changed)
        self.ui.sbWindowSize.setEnabled(False)
        self.ui.sbWorldSize.setValue(10)

    def visualization_type_changed(self):
        self.ui.sbWindowSize.setEnabled(self.ui.cbOutType.currentIndex() == 1)

    def button_click(self):
        self.run_life()

    def run_life(self):
        dic = {}
        check_repeat = self.ui.cbCheckRepeat.isChecked()
        world = LifeWorld(self.ui.sbWorldSize.value(), self.ui.cbRandomInit.isChecked())
        # vm = input("select viewer: 0 - text, 1 - graphics\n")
        # if vm not in {'0', '1'}:
        #    raise Exception("error")

        if self.ui.cbOutType.currentIndex() == 0:
           viewer = LifeViewer()
        else:
           viewer = TurtleViewer(self.ui.sbWindowSize.value(), self.ui.sbWindowSize.value())

        while world.next_generation():
            if check_repeat:
                _hash = world.get_hash()
                val = dic.get(_hash)
                if val is None:
                    dic[_hash] = world.get_generation()
                else:
                    break
            viewer.show_world(world, False, '')
            #    viewer.show_world(world)
            time.sleep(self.ui.dsbDelay.value())

        legend = ''
        print("-------------COMPLETION OF EVOLUTION  {}-----------------".format(world.get_generation()))

        if world.get_empty():
            legend = "-------------EXTINCTION IN GENERATION {}-----------------".format(world.get_generation())
        else:
            _hash = world.get_hash()
            gen = dic.get(_hash)
            if gen is not None:
                if world.get_generation() - gen == 1:
                    legend = "-------------STABLE CONFIGURATION IN GENERATION {}-----------------".format(gen)
                else:
                    legend = "-------------REPEAT CONFIGURATION FROM GENERATION {}-----------------".format(gen)

        viewer.show_world(world, True, legend)
        print(legend)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())


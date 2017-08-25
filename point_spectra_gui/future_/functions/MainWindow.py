import pickle

from PyQt5 import QtWidgets

from point_spectra_gui.ui import MainWindow


class Ui_MainWindow(MainWindow.Ui_MainWindow):
    def __init__(self):
        self.widget = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)  # Run the basic window UI
        self.menu_item_shortcuts()  # set up the shortcuts

    def addWidget(self, obj):
        """
        Add a layout to the MainWindow
        :param obj:
        :return:
        """
        self.widget = obj()
        self.widget.setupUi(self.scrollArea)
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.widgetLayout.addWidget(self.widget.get_widget())

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")
        self.actionCreate_New_Workflow.setShortcut("ctrl+N")
        self.actionOpen_Workflow.setShortcut("ctrl+O")
        self.actionRestore_Workflow.setShortcut("ctrl+R")
        self.actionSave_Current_Workflow.setShortcut("ctrl+S")

    def addWidgetList(self, widgetList):
        """
        Add the pysat_list algorithm here
        This and addWidget() will be working together
        :param widgetList:
        :return:
        """
        self.widget

    def getAllParams(self):
        pass

    def on_save_clicked(self):
        """
        Save the workflow to a *.wrd file
        :return:
        """
        try:
            filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None,
                                                                      "Choose where you want save your file",
                                                                      '.',
                                                                      '(*.wrf)')
            print(filename)
            with open(filename, 'wb') as fp:
                pickle.dump((), fp)
        except:
            print("File not loaded")

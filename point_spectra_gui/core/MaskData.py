from PyQt5 import QtWidgets

from point_spectra_gui.ui.MaskData import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.util.SingleData import SingleData


class MaskData(Ui_Form, SingleData):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Mask Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def updateWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)

    def connectWidgets(self):
        self.pushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.maskFileLineEdit))
        [self.chooseDataComboBox.currentIndexChanged.connect(x) for x in [self.setCurrentData, self.set_data_idx]]

    def run(self):
        datakey = self.chooseDataComboBox.currentText()
        maskfile = self.maskFileLineEdit.text()
        self.data[datakey].mask(maskfile, maskvar='wvl')
        print("Mask applied")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = MaskData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

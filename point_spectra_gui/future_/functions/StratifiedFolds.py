from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.StratifiedFolds import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataToStratifyComboBox, self.datakeys)
        self.chooseDataToStratifyComboBox.activated[int].connect(self.strat_fold_change_vars)
        self.nFoldsSpinBox.valueChanged.connect(self.strat_fold_change_testfolds)

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        datakey = self.chooseDataToStratifyComboBox.currentText()
        nfolds = self.nFoldsSpinBox.value()
        try:
            testfold = int(self.testFoldsSpinBox.currentText())
        except:
            testfold = 1
        colname = ('comp', self.chooseVarComboBox.currentText())
        self.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)

        self.data[datakey + '-Train'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        self.data[datakey + '-Test'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        self.datakeys = self.data.keys()

        print(self.data.keys())
        print(self.data[datakey + '-Test'].df.index.shape)
        print(self.data[datakey + '-Train'].df.index.shape)

    def strat_fold_change_vars(self):
        self.chooseVarComboBox.clear()
        try:
            choices = self.data[self.chooseDataToStratifyComboBox.currentText()].df['comp'].columns.values
        except:
            choices = ['No composition columns!']

        self.chooseVarComboBox.addItems(choices)

    def strat_fold_change_testfolds(self):
        self.testFoldsSpinBox.clear()
        self.testFoldsSpinBox.setMaximum(self.nFoldsSpinBox.value())

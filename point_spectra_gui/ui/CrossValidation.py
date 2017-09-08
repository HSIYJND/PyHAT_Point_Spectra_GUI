# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\PySAT_Point_Spectra_GUI\ui\CrossValidation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regression = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.regression.setFont(font)
        self.regression.setObjectName("regression")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.regression)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.regression_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosedata_hlayout.setObjectName("regression_choosedata_hlayout")
        self.regression_choosedata_label = QtWidgets.QLabel(self.regression)
        self.regression_choosedata_label.setObjectName("regression_choosedata_label")
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata_label)
        self.regression_choosedata = QtWidgets.QComboBox(self.regression)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName("regression_choosedata")
        self.regression_choosedata.addItem("")
        self.regression_choosedata.addItem("")
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_choosedata_hlayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.regression_choosedata_hlayout)
        self.regression_choosevars_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosevars_hlayout.setObjectName("regression_choosevars_hlayout")
        self.regression_choosex_vlayout = QtWidgets.QVBoxLayout()
        self.regression_choosex_vlayout.setObjectName("regression_choosex_vlayout")
        self.regression_choosex_label = QtWidgets.QLabel(self.regression)
        self.regression_choosex_label.setObjectName("regression_choosex_label")
        self.regression_choosex_vlayout.addWidget(self.regression_choosex_label)
        self.regression_choosex = QtWidgets.QListWidget(self.regression)
        self.regression_choosex.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regression_choosex.sizePolicy().hasHeightForWidth())
        self.regression_choosex.setSizePolicy(sizePolicy)
        self.regression_choosex.setMinimumSize(QtCore.QSize(0, 0))
        self.regression_choosex.setMaximumSize(QtCore.QSize(900, 16777215))
        self.regression_choosex.setObjectName("regression_choosex")
        item = QtWidgets.QListWidgetItem()
        self.regression_choosex.addItem(item)
        self.regression_choosex_vlayout.addWidget(self.regression_choosex)
        self.regression_choosevars_hlayout.addLayout(self.regression_choosex_vlayout)
        self.regression_choosey_vlayout = QtWidgets.QVBoxLayout()
        self.regression_choosey_vlayout.setObjectName("regression_choosey_vlayout")
        self.regression_choosey_label = QtWidgets.QLabel(self.regression)
        self.regression_choosey_label.setObjectName("regression_choosey_label")
        self.regression_choosey_vlayout.addWidget(self.regression_choosey_label)
        self.regression_choosey = QtWidgets.QListWidget(self.regression)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regression_choosey.sizePolicy().hasHeightForWidth())
        self.regression_choosey.setSizePolicy(sizePolicy)
        self.regression_choosey.setMinimumSize(QtCore.QSize(0, 0))
        self.regression_choosey.setMaximumSize(QtCore.QSize(900, 16777215))
        self.regression_choosey.setObjectName("regression_choosey")
        item = QtWidgets.QListWidgetItem()
        self.regression_choosey.addItem(item)
        self.regression_choosey_vlayout.addWidget(self.regression_choosey)
        self.regression_choosevars_hlayout.addLayout(self.regression_choosey_vlayout)
        self.verticalLayout_2.addLayout(self.regression_choosevars_hlayout)
        self.min_max_layout = QtWidgets.QHBoxLayout()
        self.min_max_layout.setObjectName("min_max_layout")
        self.min_label = QtWidgets.QLabel(self.regression)
        self.min_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.min_label.setObjectName("min_label")
        self.min_max_layout.addWidget(self.min_label)
        self.yvarmin_spin = QtWidgets.QDoubleSpinBox(self.regression)
        self.yvarmin_spin.setMaximum(9999999.0)
        self.yvarmin_spin.setObjectName("yvarmin_spin")
        self.min_max_layout.addWidget(self.yvarmin_spin)
        self.max_label = QtWidgets.QLabel(self.regression)
        self.max_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.max_label.setObjectName("max_label")
        self.min_max_layout.addWidget(self.max_label)
        self.yvarmax_spin = QtWidgets.QDoubleSpinBox(self.regression)
        self.yvarmax_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.yvarmax_spin.setDecimals(2)
        self.yvarmax_spin.setMinimum(0.0)
        self.yvarmax_spin.setMaximum(9999999.0)
        self.yvarmax_spin.setProperty("value", 100.0)
        self.yvarmax_spin.setObjectName("yvarmax_spin")
        self.min_max_layout.addWidget(self.yvarmax_spin)
        self.verticalLayout_2.addLayout(self.min_max_layout)
        self.regression_alg_choices = QtWidgets.QComboBox(self.regression)
        self.regression_alg_choices.setMinimumSize(QtCore.QSize(250, 0))
        self.regression_alg_choices.setIconSize(QtCore.QSize(50, 20))
        self.regression_alg_choices.setObjectName("regression_alg_choices")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.verticalLayout_2.addWidget(self.regression_alg_choices)
        self.algorithmLayout = QtWidgets.QVBoxLayout()
        self.algorithmLayout.setObjectName("algorithmLayout")
        self.verticalLayout_2.addLayout(self.algorithmLayout)
        self.verticalLayout.addWidget(self.regression)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.regression_choosedata, self.regression_choosex)
        Form.setTabOrder(self.regression_choosex, self.regression_choosey)
        Form.setTabOrder(self.regression_choosey, self.yvarmin_spin)
        Form.setTabOrder(self.yvarmin_spin, self.yvarmax_spin)
        Form.setTabOrder(self.yvarmax_spin, self.regression_alg_choices)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.regression.setTitle(_translate("Form", "Cross Validation/Training"))
        self.regression_choosedata_label.setText(_translate("Form", "Choose data:"))
        self.regression_choosedata.setItemText(0, _translate("Form", "Choose Data"))
        self.regression_choosedata.setItemText(1, _translate("Form", "Known Data"))
        self.regression_choosex_label.setText(_translate("Form", "X Variable:"))
        __sortingEnabled = self.regression_choosex.isSortingEnabled()
        self.regression_choosex.setSortingEnabled(False)
        item = self.regression_choosex.item(0)
        item.setText(_translate("Form", "Choose X"))
        self.regression_choosex.setSortingEnabled(__sortingEnabled)
        self.regression_choosey_label.setText(_translate("Form", "Y Variable:"))
        self.regression_choosey.setSortingEnabled(True)
        __sortingEnabled = self.regression_choosey.isSortingEnabled()
        self.regression_choosey.setSortingEnabled(False)
        item = self.regression_choosey.item(0)
        item.setText(_translate("Form", "Choose Y"))
        self.regression_choosey.setSortingEnabled(__sortingEnabled)
        self.min_label.setText(_translate("Form", "Min:"))
        self.max_label.setText(_translate("Form", "Max:"))
        self.regression_alg_choices.setItemText(0, _translate("Form", "Choose an algorithm"))
        self.regression_alg_choices.setItemText(1, _translate("Form", "PLS"))
        self.regression_alg_choices.setItemText(2, _translate("Form", "GP"))
        self.regression_alg_choices.setItemText(3, _translate("Form", "OLS"))
        self.regression_alg_choices.setItemText(4, _translate("Form", "OMP"))
        self.regression_alg_choices.setItemText(5, _translate("Form", "Lasso"))
        self.regression_alg_choices.setItemText(6, _translate("Form", "Lasso LARS"))
        self.regression_alg_choices.setItemText(7, _translate("Form", "Elastic Net"))
        self.regression_alg_choices.setItemText(8, _translate("Form", "Ridge"))
        self.regression_alg_choices.setItemText(9, _translate("Form", "More to come..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


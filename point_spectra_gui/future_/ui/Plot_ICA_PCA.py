from point_spectra_gui.future_.ui.UI_Plot_ICA_PCA import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupbox

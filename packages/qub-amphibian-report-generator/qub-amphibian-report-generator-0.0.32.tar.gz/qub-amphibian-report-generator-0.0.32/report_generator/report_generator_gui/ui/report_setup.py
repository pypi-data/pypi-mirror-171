# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_generator/report_generator_gui/ui/setup.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from report_generator.project_setup.new_report_project import create_new_project


class Ui_Dialog(object):
    def setupUi(self, Dialog, ui):
        Dialog.setObjectName("Dialog")
        Dialog.resize(433, 300)
        self.dialogwin = Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 411, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.reportNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.reportNameLabel.setObjectName("reportNameLabel")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.reportNameLabel
        )
        self.reportNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reportNameLineEdit.setObjectName("reportNameLineEdit")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.reportNameLineEdit
        )
        self.reportAuthorLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.reportAuthorLabel.setObjectName("reportAuthorLabel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.reportAuthorLabel
        )
        self.reportAuthorLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reportAuthorLineEdit.setObjectName("reportAuthorLineEdit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.reportAuthorLineEdit
        )
        self.universityNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.universityNameLabel.setObjectName("universityNameLabel")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.universityNameLabel
        )
        self.universityNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.universityNameLineEdit.setObjectName("universityNameLineEdit")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.universityNameLineEdit
        )
        self.universitySchoolLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.universitySchoolLabel.setObjectName("universitySchoolLabel")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.universitySchoolLabel
        )
        self.universitySchoolLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.universitySchoolLineEdit.setObjectName("universitySchoolLineEdit")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.universitySchoolLineEdit
        )
        self.defaultReportNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.defaultReportNameLabel.setObjectName("defaultReportNameLabel")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.defaultReportNameLabel
        )
        self.defaultReportNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.defaultReportNameLineEdit.setObjectName("defaultReportNameLineEdit")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.defaultReportNameLineEdit
        )
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 190, 111, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 190, 161, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 190, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_button)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 431, 41))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.report_setup_ok_button)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.ui = ui

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Project Set Up"))
        self.reportNameLabel.setText(_translate("Dialog", "Project Name"))
        self.reportAuthorLabel.setText(_translate("Dialog", "Default Report Author"))
        self.universityNameLabel.setText(
            _translate("Dialog", "Default University Name")
        )
        self.universitySchoolLabel.setText(
            _translate("Dialog", "Default University School")
        )
        self.defaultReportNameLabel.setText(_translate("Dialog", "Default Report Name"))
        self.label.setText(_translate("Dialog", "Data Set File"))
        self.pushButton.setText(_translate("Dialog", "Browse Files"))
        self.label_6.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p><span style=" font-size:16pt; font-weight:600;">Create New Project</span></p></body></html>',
            )
        )

    def browse_button(self):
        fname = QtWidgets.QFileDialog.getOpenFileName()
        print(fname)
        self.lineEdit.setText(fname[0])

    def report_setup_ok_button(self):
        project_name = self.reportNameLineEdit.text()
        author_name = self.reportAuthorLineEdit.text()
        uni_name = self.universityNameLineEdit.text()
        school_name = self.universitySchoolLineEdit.text()
        report_name = self.defaultReportNameLineEdit.text()
        data_set = self.lineEdit.text()

        print("hello")
        settings = {
            "project_name": project_name,
            "report_name": report_name,
            "author_name": author_name,
            "school_name": school_name,
            "uni_name": uni_name,
            "data_set": data_set,
        }

        create_new_project(settings)
        self.show_popup()
        self.ui.set_config_values()
        self.ui.load_font_selection_combo()
        self.dialogwin.close()

    def show_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Setup Complete")
        msg.setText("Report-Generator setup complete.")
        msg.exec_()

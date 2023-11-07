import sys
import os
from PyQt5 import QtWidgets, QtGui
from lab31 import create_annotation_file
from lab34 import get_next_instance

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dataset Annotation App")
        self.setGeometry(100, 100, 600, 400)

        self.dataset_path_label = QtWidgets.QLabel("Select the dataset folder:")
        self.dataset_path_line_edit = QtWidgets.QLineEdit()
        self.browse_button = QtWidgets.QPushButton("Browse")
        self.create_annotation_button = QtWidgets.QPushButton("Create Annotation File")
        self.next_tiger_button = QtWidgets.QPushButton("Next Tiger")
        self.next_leopard_button = QtWidgets.QPushButton("Next Leopard")
        self.image_label = QtWidgets.QLabel()
        self.image_label.setScaledContents(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.dataset_path_label)
        layout.addWidget(self.dataset_path_line_edit)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.create_annotation_button)
        layout.addWidget(self.next_tiger_button)
        layout.addWidget(self.next_leopard_button)
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        self.browse_button.clicked.connect(self.browse_dataset)
        self.create_annotation_button.clicked.connect(self.create_annotation)
        self.next_tiger_button.clicked.connect(self.display_next_tiger)
        self.next_leopard_button.clicked.connect(self.display_next_leopard)

    def browse_dataset(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.dataset_path_line_edit.setText(folderpath)

    def create_annotation(self):
        dataset_path = self.dataset_path_line_edit.text()
        if dataset_path:
            output_file, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Output File', filter='CSV Files (*.csv)')
            if output_file:
                create_annotation_file(dataset_path, output_file)
                QtWidgets.QMessageBox.information(self, "Annotation Created", f"Annotation file {output_file} created successfully.")

    def display_next_tiger(self):
        next_tiger = get_next_instance('tiger')
        if next_tiger:
            pixmap = QtGui.QPixmap(next_tiger)
            self.image_label.setPixmap(pixmap)

    def display_next_leopard(self):
        next_leopard = get_next_instance('leopard')
        if next_leopard:
            pixmap = QtGui.QPixmap(next_leopard)
            self.image_label.setPixmap(pixmap)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

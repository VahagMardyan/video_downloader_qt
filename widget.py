# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ui_form import Ui_Widget
from worker import DownloadWorker

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.btn_download.clicked.connect(self.start_download)
        self.ui.link.returnPressed.connect(self.start_download)
        self.ui.btn_cancel.clicked.connect(self.cancel_download)
        self.ui.progressBar.setValue(0)

    def start_download(self):
        url = self.ui.link.text().strip()
        media_format = "mp3" if self.ui.checkBox.isChecked() else "mp4"

        if not url:
            QMessageBox.warning(self, "Error", "Please enter an URL")
            return

        self.ui.progressBar.setValue(0)
        self.ui.btn_download.setEnabled(False)
        self.ui.btn_cancel.setEnabled(True)

        self.thread = QThread()
        self.worker = DownloadWorker(url, media_format)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.ui.progressBar.setValue)
        self.worker.finished.connect(self.on_finished)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def cancel_download(self):
        if hasattr(self, "worker"):
                self.worker.cancel()
                self.ui.btn_cancel.setEnabled(False)

    def on_finished(self, message: str, ok: bool):
        self.ui.btn_download.setEnabled(True)
        self.ui.btn_cancel.setEnabled(False)
        if ok:
            QMessageBox.information(self, "Download Completed", message)
        else:
            QMessageBox.critical(self, "Download Error", message)


def load_stylesheet(app):
        with open("style.qss", "r", encoding="utf-8") as f:
                app.setStyleSheet(f.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_stylesheet(app)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

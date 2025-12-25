from PySide6.QtCore import QObject, Signal
from core import download_media

class DownloadWorker(QObject):
    progress = Signal(int)
    finished = Signal(str, bool)
    def __init__(self, url, fmt):
        super().__init__()
        self.url = url
        self.fmt = fmt
        self.is_cancelled = False

    def cancel(self):
        self.is_cancelled = True

    def run(self):
        def on_progress(d):

            if self.is_cancelled:
                raise Exception("Download cancelled by user")

            if d["status"] == "downloading":
                total = d.get("total_bytes") or d.get("total_bytes_estimate")
                downloaded = d.get("downloaded_bytes",0)

                if total:
                    percent = int(downloaded * 100 / total)
                    self.progress.emit(percent)

        try:
            message, ok = download_media(self.url, self.fmt, progress_callback=on_progress)
            self.finished.emit(message, ok)
        except Exception as e:
            self.finished.emit(str(e), False)

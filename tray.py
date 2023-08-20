from PyQt5.QtWidgets import QMenu, QSystemTrayIcon, QAction, QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
import sys


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, handlers, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)
        menu = QMenu(parent)

        checkableAction = QAction("Keep muted", parent)
        checkableAction.setCheckable(True)
        checkableAction.triggered.connect(handlers["on_toggle_keep_unmuted"])
        menu.addAction(checkableAction)

        intervalAction = QAction("Change target interval", parent)
        intervalAction.triggered.connect(handlers["on_change_interval"])
        menu.addAction(intervalAction)

        volumeAction = QAction("Change target volume", parent)
        volumeAction.triggered.connect(handlers["on_change_volume"])
        menu.addAction(volumeAction)

        exitAction = QAction("Exit", parent)
        exitAction.triggered.connect(QCoreApplication.instance().quit)
        exitAction.triggered.connect(handlers["exit_handler"])
        menu.addAction(exitAction)

        self.setContextMenu(menu)


def create_tray_icon(handlers):
    app = QApplication([])
    widget = QWidget()

    tray_icon = SystemTrayIcon(QIcon("icon.ico"), handlers, widget)
    tray_icon.show()

    sys.exit(app.exec_())

# This Python file uses the following encoding: utf-8
import datetime
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
from gateways.binance.binance_gateway import BinanceGateway
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.ui_form import Ui_MainWindow
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.log_widget.setHorizontalHeaderLabels(["时间", "内容"])
        self.ui.actionBinance.triggered.connect(self.open_connect)

    def open_connect(self):
        gateway_obj = BinanceGateway()
        if not gateway_obj.test_connect():
            self.write_log("Binance连接失败")
            return
        self.write_log("Binance连接成功")
        # 获取品种
        symbols = gateway_obj.get_all_symbols()
        for symbol in symbols:
            self.ui.symbol_combo_box.addItem(symbol)




    def write_log(self, message):
        # 在最后插入一行
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.log_text.append(f"{now_time}  {message}")
        self.ui.log_text.ensureCursorVisible()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

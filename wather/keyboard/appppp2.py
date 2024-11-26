import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow

from crawler import GoogleWather

# ui = uic.loadUiType("untitled.ui")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "ui", "app.ui")
        print("ui path:", ui_path) #디버깅용
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI 파일이 존재하지 않습니다.: {ui_path}")
            # UI 파일 로드
        uic.loadUi(ui_path, self)

        self.pushButton.clicked.connect(self.run)
        self.crawler = GoogleWeather()

    def run(self):
        keybord = self.lineEdit.text()
        # print(f"키워드 입력 : {keyword}") #이건 디버그용
        self.craler.set_keyword(keyword + '날씨')    
        self.crawler.run()
        result = self.crawler.get_result()
        print(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
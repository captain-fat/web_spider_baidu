from main_window import Ui_MainWindow
from PyQt5.QtWidgets import  QMainWindow, QApplication
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import time
import urllib
import re
import sys

class my_main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(my_main_window, self).__init__()
        self.setupUi(self)
        self.btn_start.clicked.connect(self.read_imput_text)
        self.btn_start.clicked.connect(self.get_words)


    def read_imput_text(self):
        input_text = self.text_inputbox.toPlainText()
        #配置浏览器，关闭界面
        chrome_opt = Options()
        chrome_opt.add_argument('---windows-size=1366,768')
        chrome_opt.add_argument('--headless')
        chrome_opt.add_argument('--disable-pu')
        #配置url
        url = "http://www.baidu.com/s"
        data = {'wd':input_text}
        full_url = url + '?' + urllib.parse.urlencode(data)
        #获取页面源码
        browser = webdriver.Chrome(options=chrome_opt)
        browser.get(full_url)
        time.sleep(2)
        self.page = browser.page_source
        #print(self.page)
        browser.quit()


    def get_words(self):
        #正则表达式，提取关键词
        pattern = re.compile(r'<div\s+class="(result|result-op)\s+c-container\s+.*?<a.*?>(.*?)</a>', re.I | re.S)
        results = re.finditer(pattern, self.page)
        result = []
        for i in results:
            result.append(i.group(2))
        pattern_clean = re.compile(r"<em>|</em>|'|\[|\]", re.I | re.S)
        clean_result = re.sub(pattern_clean, '', str(result))
        self.text_outputbox.setText(clean_result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = my_main_window()
    myWin.show()
    sys.exit(app.exec())


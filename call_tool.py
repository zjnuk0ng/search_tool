#coding=utf-8

from cgitb import text
import sys
import re
import time 
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_Form #载入页面
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)


    def on_googlepushButton_clicked(self): #google爬取

        name=""
        name=self.lineEdit.text()

        if name=="":
            self.textlob.append("请输入论文名称")
        else:
            self.textlob.append("正在查找...")
            findlink=re.compile(r'<a href="/scholar.*?hl=zh-CN">被引用次数：(.*?)</a>') #正则规则
            findlink2=re.compile(r'<div class="gs_r".*?</b> - 与所有文章(.*?)<br/><br/>建议.*?</a></div></div>')
        
            chrome_options = Options()
            chrome_options.add_argument('--headless') #隐藏执行
            chrome_options.add_argument("blink-settings=imagesEnabled=false")
            driver=webdriver.Chrome(chrome_options=chrome_options)
            #drive=webdriver.chrome() 测试模拟浏览器

            url='https://scholar.google.com/'
            driver.get(url)

            EC_title=EC.title_contains('Google 学术搜索')
            self.textlob.append("进入Google")

            driver.find_element_by_id("gs_hdr_tsi").send_keys(name)
            driver.find_element_by_id("gs_hdr_tsb").click()
            html = driver.page_source
            soup=BeautifulSoup(html,"html.parser")

            self.textlob.append("分析页面")

            n=1
            if n==1:
                try: #可以找到
                    for item in soup.find_all('div',class_="gs_r gs_or gs_scl"):
                        item=str(item)
                        link =re.findall(findlink,item)
                        self.googletextBrowser.setText(str(link))
                        self.textlob.append("完成！")
                        n=0 

                except:
                    print()
            if n==1:
                try: #无法找到
                    for item in soup.find_all('div',class_="gs_r"):
                        item=str(item)
                        link=re.findall(findlink2,item)
                        self.googletextBrowser.setText(str(link))
                        self.textlob.append("未找到该文章！")

                except:
                    print()

            driver.close()         

    
    def on_cleanButton_clicked(self): #清除
        self.lineEdit.clear()
        self.googletextBrowser.clear()
        self.webtextBrowser.clear()        

    def on_webpushButton_clicked(self):
        self.textlob.append("正在查找...")

        username=self.userlineEdit.text()
        password=self.passwordlineEdit.text()
        name=""
        name=self.lineEdit.text()

        if name=="":
            self.textlob.append("请输入论文名称")
        else:

            chrome_options = Options()
            #chrome_options.add_argument('--headless')
            chrome_options.add_argument("blink-settings=imagesEnabled=false")
            driver=webdriver.Chrome(chrome_options=chrome_options) 

            #driver=webdriver.Chrome()

            url = 'https://webvpn.zjnu.edu.cn/http/77726476706e69737468656265737421f1e2559434357a467b1ac7b6925b367b621b2f49c7b0/authserver/login?service=https%3A%2F%2Fwebvpn.zjnu.edu.cn%2Flogin%3Fcas_login%3Dtrue'
            driver.get(url)

            time.sleep(2)

            driver.find_element_by_name("username").send_keys(username)
            driver.find_element_by_id("password").send_keys(password)
            driver.find_element_by_class_name("auth_login_btn").click()

            time.sleep(2)

            EC_title=EC.title_contains('资源访问控制系统 - 资源站点')
            self.textlob.append("浙师大内网")
        
            curWindowHandle = driver.current_window_handle #获得原始网页句柄
            print(curWindowHandle)

            #driver.find_element_by_class_name("portal-quick-access-btn").click()
            #driver.find_element_by_class_name("portal-search__input").send_keys("www.webofknowledge.com")
            #driver.find_element_by_class_name("portal-search__button").click()

            driver.find_element_by_xpath("//h2[contains(text(), 'Web of Science')]").click()
        
            time.sleep(2)     

            allHandles = driver.window_handles #获得新打开网页的句柄
            print(f"allHandles = {allHandles}")

            for item in allHandles:         #focus到新打开的页面
                if item!=curWindowHandle:
                    driver.switch_to.window(item)

            time.sleep(2)

            try:
                driver.find_element_by_name("search-main-box").send_keys(name)
                driver.find_element_by_css_selector(".mat-focus-indicator.search > span.mat-button-wrapper").click()
                self.textlob.append("进入数据库")
            except:
                print()
                self.textlob.append("进入数据库失败！")

            time.sleep(2)

            findlink=re.compile(r'<div class="citations ng-star-inserted"><a aria-label=.*?role="link">(.*?)</a><!-- --><div class="font-size-14 data-box-text">被引频次</div><!-- --></div>')

            html = driver.page_source
            soup=BeautifulSoup(html,"html.parser")

            try:
                for item in soup.find_all('div',class_="citations ng-star-inserted"):
                    item=str(item)
                    link =re.findall(findlink,item)
                    #print(item)
                    #print(link)
                self.webtextBrowser.setText(str(link))
                self.textlob.append("完成")
            except:
                print()
                self.textlob.append("未找到该文章！")



    def on_testpushButton_clicked(self):
        self.textlob.append("尝试登录...")

        user=self.userlineEdit.text()
        pas=self.passwordlineEdit.text()

        chrome_options = Options()
        chrome_options.add_argument('--headless')

        driver=webdriver.Chrome(chrome_options=chrome_options)

        url = 'https://webvpn.zjnu.edu.cn/http/77726476706e69737468656265737421f1e2559434357a467b1ac7b6925b367b621b2f49c7b0/authserver/login?service=https%3A%2F%2Fwebvpn.zjnu.edu.cn%2Flogin%3Fcas_login%3Dtrue'
        driver.get(url)

        time.sleep(2)

        driver.find_element_by_name("username").send_keys(user)
        driver.find_element_by_id("password").send_keys(pas)
        driver.find_element_by_class_name("auth_login_btn").click()
        time.sleep(2)

        EC_title=EC.title_contains('资源访问控制系统 - 资源站点')
        self.textlob.append("进入资源访问控制系统")

        res=driver.find_element_by_class_name("wrdvpn-navbar__user").text
        driver.close() 

        if (res==user):
            self.testtextBrowser.setText("登录成功！")
            self.textlob.append("登录成功!")      
        else:
            self.testtextBrowser.setText("登录失败！")
            self.textlob.append("登录失败!")        
   

if __name__ == "__main__":
    #程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())       
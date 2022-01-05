from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from selenium.webdriver import ActionChains
from datetime import datetime
import re


class Timing:
    def __init__(self):
        self.CodeCount=[]
        self.SavedCode=[]
        self.weblist=[]
        self.biglist=[]
        self.Result=[]
        self.SavedDepth=[]
        self.usedepth = []
        with open("stock.txt","r+",encoding="utf-8") as f:
            for line in f.readlines():
                if 'A' in line:
                    if line[0:6].isnumeric():
                        self.SavedCode.append(line[0:6])
                        depth=re.findall("[0-9]+.[0-9]+",line)
                        self.SavedDepth.append(depth[-1])
                        self.SavedDepth.append(depth[-2])

                else:
                    continue
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe', options=options)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")  # 东方财金网址输入



    def Entercode(self):

        for i in range(len(self.SavedCode)):
            self.CodeCount.append(self.SavedCode[i])
            self.usedepth=self.SavedDepth[0:2]
            del self.SavedDepth[0:2]

            while True:
                try:
                    Entry = self.driver.find_element_by_xpath("//*[@id='search_box']")
                    Entry.clear()
                    Entry.send_keys(self.SavedCode[i])
                    Inf = self.driver.find_element_by_xpath("//*[@id='suggest_wrapper']/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/span")
                    Inf.click()
                    new_window = self.driver.window_handles[1]  # 转换到跳转新网页元素
                    self.driver.switch_to.window(new_window)
                    break
                except:
                    continue

            self.stockpage()


        self.driver.quit()

    def stockpage(self):

        '''
        while True:
            try:
                new_window = self.driver.window_handles[1]  # 转换到跳转新网页元素
                self.driver.switch_to.window(new_window)
                break
            except:
                continue
        '''





        while True:
            try:
                dayy = self.driver.find_element_by_xpath("//*[@id='changektab']/span[1]")
                dayy.click()  # 点击日K按钮
                break
            except:
                continue

        map = self.driver.find_element_by_css_selector("#emchartk > div.__ui")
        ActionChains(self.driver).move_to_element(map).perform()

        Button = self.driver.find_element_by_css_selector('#beforeBackRight > i')
        action = ActionChains(self.driver)
        action.move_to_element(Button).perform()

        Button1 = self.driver.find_element_by_css_selector("#beforeBackRight > dl > dd:nth-child(2)")
        Button1.click()
        pyautogui.moveTo(1300, 560)
        time.sleep(1)
        self.mousemovement()

        self.calculating1()
        self.Result=[]

        self.driver.close()
        new_window = self.driver.window_handles[0]  # 跳转回主页网页元素
        self.driver.switch_to.window(new_window)
        time.sleep(1)


    def mousemovement(self):
        for i in range(1015, 565, -6):  # 鼠标移动
            pyautogui.moveTo(i, 560)
            inf = self.driver.find_elements_by_css_selector(
                "#emchartk > div.__ui > div.__popfloatwin > h4 > span,#emchartk > div.__ui > div.__popfloatwin > div:nth-child(3) > span,#emchartk > div.__ui > div.__popfloatwin > div:nth-child(4) > span,#emchartk > div.__ui > div.__popfloatwin > div:nth-child(5) > span")
            if inf == []:
                return
                # pyautogui.moveTo(1800, 1030)
                # pyautogui.moveTo(855, 1030, 0.5)
                # continue

            self.collecting(inf)  # 开始收集数据

            if len(self.biglist) ==1:  # 处理满足条件的数据
                for i in self.biglist:
                    self.Result.append(i)
                print(self.Result)
                self.biglist=[]


                return

        self.biglist = []

    def collecting(self, inf):
        if len(self.biglist) == 0 or inf[0].text != self.biglist[-1][0]:
            for i in inf:
                if i.text == '':
                    continue
                self.weblist.append(i.text)
            # print(self.weblist)
            if len(self.weblist) == 0:  # 如果weblist里面没收集到数据
                return
            self.biglist.append(self.weblist)
            self.weblist = []

    def calculating1(self):
        if float(self.Result[-1][1])<float(self.usedepth[1]) and float(self.Result[-1][3])>float(self.usedepth[0]):
            with open("Timing.txt", "a", encoding="utf-8") as f:
                f.write(self.CodeCount[-1]+":买")
            print("牛")

        elif float(self.Result[-1][3])<float(self.usedepth[0]):
            with open("Timing.txt", "a", encoding="utf-8") as f:
                f.write(self.CodeCount[-1]+":删")
                f.write('\n')

        else:
            with open("Timing.txt", "a", encoding="utf-8") as f:
                f.write(self.CodeCount[-1]+":不符合条件")
                f.write('\n')








p=Timing()
p.Entercode()

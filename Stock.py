from selenium import webdriver
import time
import pyautogui
from selenium.webdriver import ActionChains
from datetime import datetime


class stock:
    def __init__(self):
        self.biglist = []
        self.weblist = []
        self.FinalResult1 = []
        self.CheckDouble = []
        self.SavedCode = []
        with open('stock.txt', 'r+', encoding="utf-8") as f:  # 记录操作日期
            # f.truncate(0)#清空所有数据
            for line in f.readlines():
                self.SavedCode.append(line[0:6])

            now = datetime.today()
            Data = now.strftime('%d/%m/%Y')
            if Data[0:6] not in self.SavedCode:
                f.write(Data)
                f.write('\n')

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe', options=options)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        # self.driver.get("https://quote.eastmoney.com/center/gridlist.html#kcb_board")
        self.driver.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")  # 东方财金网址输入

    def processing(self):
        self.Stock_id = []
        maxpage = self.driver.find_element_by_css_selector(
            ".dataTables_wrapper div>.paginate_page>a:nth-last-child(1)").text
        correct = ["6", "0", "3"]
        # 找出最大页数
        while True:
            i = 0
            while i < 20:
                try:
                    self.Stock_code = self.driver.find_elements_by_xpath(
                        "//*[@id='table_wrapper-table']/tbody/tr/td[2]/a")[i]
                    if self.Stock_code.text[0] not in correct:
                        i = i + 1
                        continue
                    self.Stock_id.append(self.Stock_code.text)
                    self.clickcode(self.Stock_code)
                except:
                    continue

                i += 1
            '''
            #self.Stock_code = self.driver.find_elements_by_css_selector("#table_wrapper-table > tbody > tr> td:nth-child(2) > a")
            self.Stock_code=self.driver.find_elements_by_xpath("//*[@id='table_wrapper-table']/tbody/tr/td[2]/a")

            # 拿到股票代码坐标
            for i in self.Stock_code:
                self.Stock_id.append(i.text)
                self.clickcode(i)

            '''

            checkpage = self.driver.find_element_by_css_selector(
                "#main-table_paginate > span.paginate_page > a.paginate_button.current").text
            if int(checkpage) == int(maxpage):
                self.driver.quit()
                break
            while True:
                try:
                    ChangePage = self.driver.find_element_by_css_selector(
                        "#main-table_paginate > a.next.paginate_button")
                    ChangePage.click()
                    break
                except:
                    continue
            time.sleep(1)

    def clickcode(self, key):
        key.click()
        time.sleep(1)
        new_window = self.driver.window_handles[1]  # 转换到跳转新网页元素
        self.driver.switch_to.window(new_window)
        while True:
            try:
                weekk = self.driver.find_element_by_xpath("//*[@id='changektab']/span[2]")
                weekk.click()  # 点击周K按钮
                break
            except:
                continue

        map = self.driver.find_element_by_css_selector("#emchartk > div.__ui")
        ActionChains(self.driver).move_to_element(map).perform()  # 向下滑动到周线模块

        Button = self.driver.find_element_by_css_selector('#beforeBackRight > i')
        action = ActionChains(self.driver)
        action.move_to_element(Button).perform()

        Button1 = self.driver.find_element_by_css_selector("#beforeBackRight > dl > dd:nth-child(2)")
        Button1.click()
        pyautogui.moveTo(1300, 560)

        time.sleep(1)
        self.mousemoevment()
        # self.muti()

        self.driver.close()
        new_window = self.driver.window_handles[0]  # 跳转回主页网页元素
        self.driver.switch_to.window(new_window)
        time.sleep(1)

    def mousemoevment(self):

        # 在周K图寻找规律
        # pyautogui.moveTo(885,1030)
        # pyautogui.moveTo(1800,1030,2)
        #for i in range(1015, 565, -3):

        for i in range(1015, 565, -3):  # 鼠标移动(坐标，坐标，移动速度)
            pyautogui.moveTo(i, 505)
            inf = self.driver.find_elements_by_css_selector(
                "#emchartk > div.__ui > div.__popfloatwin > h4 > span,#emchartk > div.__ui > div.__popfloatwin > div:nth-child(3) > span,#emchartk > div.__ui > div.__popfloatwin > div:nth-child(4) > span,#emchartk > div.__ui > div.__popfloatwin > div:nth-child(5) > span")
            if inf == []:
                return
                # pyautogui.moveTo(1800, 1030)
                # pyautogui.moveTo(855, 1030, 0.5)
                # continue

            self.collecting(inf)  # 开始收集数据

            if len(self.biglist) == 10:  # 处理满足条件的数据
                self.calculating1()

                self.biglist = []
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

        # [0:日期，1:收盘，2:最高，3：最低]

    def calculating1(self):
        self.biglist.reverse()
        for i in range(len(self.biglist)):
            if i + 4 > len(self.biglist):
                # break
                return
            else:
                p1list = self.biglist[i:i + 4]  # 收集的四组数据
                if float(p1list[0][1]) < float(p1list[1][1]) < float(p1list[2][1]) < float(p1list[3][1]):
                    if float(p1list[2][1]) - float(p1list[1][1]) > float(p1list[1][1]) - float(p1list[0][1]):
                        self.FinalResult1.append(p1list[1])  # 趋势起点
                        self.calculating2()
                        break
                    else:
                        continue
                else:
                    continue

    def calculating2(self):
        if self.Stock_id[-1] in self.CheckDouble:##<--查看是否重复计算
            return
        x = self.biglist.index(self.FinalResult1[-1])  # 寻找起始点在是个数据里面的坐标
        for i in range(x + 1, len(self.biglist)):
            if float(self.biglist[i][1]) >= float(self.biglist[i - 1][1]) > 0:
                continue
            elif 0 < float(self.biglist[i][1]) < float(self.biglist[i - 1][1]) and i == 9:  # 判断条件2
                if 0 < (float(self.biglist[i - 1][1]) - float(self.biglist[i - 2][1])) < (
                        float(self.biglist[i - 2][1]) - float(self.biglist[i - 3][1])):

                    for a in range(i, len(self.biglist)):  # 转折点后所有周线收盘价<转折点收盘价and所有转折点以后的周线最低价都得>BC
                        if float(self.biglist[a][1]) < float(self.biglist[i - 1][1]) and float(
                                self.biglist[a][3]) > float(self.FinalResult1[-1][1]):
                            continue
                        else:
                            return
                    # 判断强弱趋势  0<NC<PL<OC
                    if 0 < float(self.biglist[i - 2][1]) < float(self.biglist[i][3]) < float(
                            self.biglist[i - 1][1]) and self.biglist[-1][1]<self.biglist[-2][1] and\
                            float(self.biglist[-2][1])-float(self.biglist[-1][2])>float(self.biglist[-1][2])-float(self.biglist[-1][3]):  #A-B>2(B-C)
                        # 判断最大回调深度
                        depth = float(self.biglist[-1][1]) - float(self.biglist[-2][1]) + float(self.biglist[-1][3])
                        with open('stock.txt', 'a', encoding="utf-8") as f:
                            # f.write(self.Stock_id[-1] + " 趋势起点:" + str(self.FinalResult1[-1]) + " 转折点:" + str(
                            # self.biglist[i - 1]) + 'A ' + "转折点后第一根周线最低价:" + self.biglist[i][3])
                            f.write(self.Stock_id[-1] + " 趋势起点:" + str(self.FinalResult1[-1]) + " 第九周第十周最高价:" + str(max( self.biglist[-1][2], self.biglist[-2][2])
                                ) + ' A ' + "第十周最低价:" + self.biglist[i][3] + "回调深度: " + str(depth)+"开仓价:"+str(depth*1.02))
                            self.CheckDouble.append(self.Stock_id[-1])
                            f.write('\n')

                        return
                    """
                    #强回调
                    elif float(self.biglist[x][1]) < float(self.biglist[i][3]) < float(self.biglist[i - 2][1]) < float(
                            self.biglist[i - 1][1]):  # BC<PL<NC<OC
                        # new
                        max1 = 0
                        for x in range(1, i - 1):
                            num1 = float(self.biglist[x][1]) - float(self.biglist[x - 1][1])
                            if num1 > max1:
                                max1 = num1

                        max2 = 0
                        for x in range(i, 10):
                            num1 = float(self.biglist[x - 1][1]) - float(self.biglist[x][3])
                            if num1 > max2:
                                max2 = num1

                        if max2 < max1:
                            with open('stock.txt', 'a', encoding="utf-8") as f:
                                '''
                                f.write(self.Stock_id[-1] + " 趋势起点:" + str(self.FinalResult1[-1]) + " 转折点:" + str(
                                    self.biglist[i - 1]) + 'B')
                                    '''
                                self.CheckDouble.append(self.Stock_id[-1])
                                f.write('\n')

                            return
                    """

    def changepage(self, page):  # 调节起始页
        Entry = self.driver.find_element_by_css_selector("#main-table_paginate > input")
        Entry.clear()
        Entry.send_keys(page)

        Go = self.driver.find_element_by_css_selector("#main-table_paginate > a.paginte_go")
        Go.click()
        time.sleep(1)
        pyautogui.scroll(400)


'''
               if float(self.biglist[1][1]) > float(self.biglist[2][1]) > float(self.biglist[3][1]) > float(
                       self.biglist[4][1]) > 0 and (float(self.biglist[2][1]) - float(self.biglist[3][1])) > (
                       float(self.biglist[3][1]) - float(self.biglist[4][1])) > 0:
                   # DC>CC>BC>AC>0 AND CC-BC>BC-AC>0
                   if float(self.biglist[0][1]) < float(self.biglist[1][1]) and 0 < (
                           float(self.biglist[1][1]) - float(self.biglist[2][1])) < (
                           float(self.biglist[2][1]) - float(self.biglist[3][1])):
                       # 0<AC<BC<CC<DC AND EC<DC AND 0<DC-CC<CC-BC
                       if 0 < float(self.biglist[2][1]) < float(self.biglist[0][3]) < float(self.biglist[1][1]):
                           # 0<CC<EL<DC
                           self.FinalResult.append([self.Stock_id[-1], "A"])#弱回调
                           print(self.FinalResult[-1])#打印最新消息
                       elif float(self.biglist[3][1]) < float(self.biglist[0][3]) < float(self.biglist[2][1]) < float(
                               self.biglist[1][1]):
                           # BC<EL<CC<DC
                           self.FinalResult.append([self.Stock_id[-1], "B"])#强回调
                           print(self.FinalResult[-1])
                       else:
                           return
                   else:
                       return
               else:
                   return

               '''

p = stock()
p.processing()


项目标题：网页自动化实现网上股票筛选
项目背景：2021年7月中旬，实习期间的一位曾经上海交易员请求用程序帮助自动筛选股票以提高工作效率

项目功能：重点为python自动化框架selenium，通过定位网页元素来进行自动化网页操作和收集，程序功能为自动进入东方财富网站的沪深京A股并且收集各种符合要求的股票数据

项目复盘和思考：本身程序的操作逻辑很简单，运用python的selenium库来定位网页元素以模仿人的网页操作，但是苦难的是如何去有效的收集数据。
1.网页中存在的一些隐藏元素需要通过鼠标特定的操作才能展现。因此需要不停移动鼠标才能收集到足够信息而不是一次性获取到所有。通过鼠标移动收集数据速度慢，效率低！
2.在鼠标移动触发颖仓元素的过程中，鼠标需要被给予特定的像素位置。但是每台电脑像素不同，所以导致如果在不同电脑上进行操作需要手动更换像素位置。
3.容易被反爬，网页元素一旦发生变化就会产生大量问题，比如大量定位元素需要修改!

更改日期：1/3/2022

Project Title: Webpage Automation Realizes Online Stock Screening
Project background: In mid-July 2021, a former Shanghai trader during the internship requested a program to help automatically screen stocks to improve work efficiency

Project function: The focus is on the python automation framework selenium, which automates web page operations and collection by locating web page elements. The program function is to automatically enter the Shanghai, Shenzhen and Beijing A shares of the Oriental Fortune website and collect various stock data that meet the requirements

Project review and thinking: The operation logic of the program itself is very simple, using python's selenium library to locate webpage elements to imitate human webpage operations, but the difficulty is how to collect data effectively.
1. Some hidden elements in the webpage need to be displayed through specific mouse operations. Therefore, you need to keep moving the mouse to collect enough information instead of acquiring all at once. Collecting data by mouse movement is slow and inefficient!
2. When the mouse moves to trigger the Yingcang element, the mouse needs to be given a specific pixel position. However, the pixels of each computer are different, so if you operate on a different computer, you need to manually change the pixel position.
3. It is easy to be crawled back. Once the web page elements are changed, a lot of problems will arise, such as a large number of positioning elements that need to be modified!

Date of change: 1/3/2022

# 安装和注意指南
* 你好

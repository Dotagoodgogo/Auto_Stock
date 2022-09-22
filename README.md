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

# 安装和注意指南（基于stock7）
# Installation and attention guide (based on stock7)
1. 请下载chromedrive到C:\Program Files (x86)目录下-->注意chromedrive的版本需要和你用的google chrome版本一致。如何检查当前chrome版本请打开chrome然后点击右上角三点然后点击help然后点击About Google Chrome。

1. Please download chromedrive to C:\Program Files (x86) directory --> Note that the version of chromedrive needs to be the same as the version of google chrome you are using. How to check the current chrome version, please open chrome and click the three dots on the top right corner and then click help and then click About Google Chrome.


2.代码部分请安装以下库，如果以下代码有下划红线线表明并没安装。

2. Code section please install the following libraries, if the following code has underlined red line indicates that it is not installed.
![image](https://user-images.githubusercontent.com/87624521/183232870-56a2a119-befb-41ae-b182-8aa6dbb81d3d.png)

pycharm用户直接鼠标移到红色部分，点击install package如下例图

pycharm users directly mouse over the red part and click on install package as shown in the following example
![image](https://user-images.githubusercontent.com/87624521/183233082-d41fde85-76c9-4df7-a6f0-f4dfa44422c7.png)

3.完成上述操作后主要修改地方为141-142行

3. After completing the above operation, the main changes are made to lines 141-142

![image](https://user-images.githubusercontent.com/87624521/183233273-54f05517-dece-42da-86cf-f3aeda5fe010.png)

首先需要搞懂这两行是什么意思

First, you need to understand what these two lines mean

1015 565是什么意思？他的意思是下图股票图标的最右边的x像素值和最左边的x像素值。

What does 1015 565 mean? He means the rightmost x pixel value and the leftmost x pixel value of the stock icon below.


![image](https://user-images.githubusercontent.com/87624521/183233388-13e41689-4d86-4bcb-808d-f7c45c6c81ea.png)

因为我们需要收集近十周的股票数据所以程序设计是从右往左自动滑动，当我们每次鼠标触发到某个周，网页的html元素会自动显示当周数据，这是我们这一个循环的工作原理。因为程序是通过像素值定位，每台电脑的像素值可能不同，所以如果需要更换电脑，程序中的一些像素值需要进行一些修改。正如我们现在所正在做的这一步。

Because we need to collect stock data for the last ten weeks, the program is designed to automatically slide from right to left. When we trigger to a certain week each time, the html element of the web page will automatically display the data of that week, this is how we work in this cycle. Because the program is positioned by pixel values, each computer may have different pixel values, so if we need to change computers, some pixel values in the program need to be modified. As we are doing now in this step.

4.如何获取股票图像的左右x值呢？我们需要以下代码

4. How to get the left and right x-values of the stock image? We need the following code

![image](https://user-images.githubusercontent.com/87624521/183233751-8dd3c14a-2f2e-4c0c-b2f7-e4b7a311b23a.png)

当然应该还有很多途径！我们首先导入库pyautogui和time然后写以下两行代码非常之简单。time.sleep(5)的意思为等待五秒。为什么要等待五秒，我之后再说。接下来是print(pyautogui.position())的意思为打印出当前鼠标x,y像素值。接下来我们启动程序打开网页下滑到图表，然后鼠标滑到图标右侧。五秒后程序会自动获取鼠标当前位置，这样我们就获得了图标最右侧的位置。当然，最左侧的方式是一样的。所以刚开始time.sleep(5)的意思是等待五秒，等你打开网页和鼠标就位的时间。如果觉得时间不够可以让等待时间更长通过更改time.sleep（）的值。

Of course there should be many more ways! We first import the library pyautogui and time and then write the following two lines of code very simple. time.sleep(5) means wait for five seconds. Why wait for five seconds, I will say later. Next is print(pyautogui.position()) which means print out the current mouse x,y pixel value. Next we start the program to open the web page slide down to the chart, and then the mouse slide to the right of the icon. After five seconds the program will automatically get the current position of the mouse, so we get the rightmost position of the icon. Of course, the leftmost way is the same. So at first time.sleep(5) means wait five seconds for you to open the page and mouse in place. If you think it's not enough time you can make the wait longer by changing the value of time.sleep().

回到141行 for loop 最后一个参数-6是鼠标一次的移动像素值，因为我们是从从右往左而不是从左往右，所以这里为-6而不是6。切记鼠标移动速度可等测试时候决定，鼠标移动像素太大可能会导致会漏读周线数据。

Back to line 141 for loop, the last parameter -6 is the pixel value of mouse movement, because we are moving from right to left instead of left to right, so here is -6 instead of 6. Remember that the mouse movement speed can be decided when testing, too much mouse movement may cause the weekly data to be missed.

5. 142 行pyautogui.moveTo(i, 505)在loop当中鼠标会一直在相同y值(这里是505)的情况横向移动，在测试中，请确保y值的范围一定要在图标的Y值区间。假如图标的Y值是从100->200。而用户y值设置为250. 这样会导致鼠标在图标之外移动从而触发不了每周周线数据。

5. 142 line pyautogui.moveTo(i, 505) In the loop, the mouse will always move horizontally with the same y value (505 in this case), in the test, please make sure that the y value range must be in the range of the icon's y value. If the y-value of the icon is from 100->200, and the y-value of the user is set to 250, this will cause the mouse to move outside the icon and thus not trigger the weekly data.

6.一些debug的方法，本程序很多定位都是通过css和xml来定位的语法为以下两个案例，或可上网查找相关文档。假如一些代码定位出现问题可以在网页上检查

6. some debug methods, this program is a lot of positioning through css and xml to position the syntax for the following two cases, or you can go online to find the relevant documents. If some code positioning problems can be checked on the web page

![image](https://user-images.githubusercontent.com/87624521/183234366-e83a8b2f-5076-4e18-91a8-b3876472b144.png)

![image](https://user-images.githubusercontent.com/87624521/183234373-1035e475-e7da-4a5c-8f7d-c8bafd4b15f9.png)

检查方法如下：
可以copy上面的css或者xpath的定位参数例如：//*[@id='app']/div/div/div[9]/div[2]/div[1]/div[1]/div[3]/ul/li[2]/a

Check the method as follows.
You can copy the above css or xpath positioning parameters for example: //*[@id='app']/div/div/div[9]/div[2]/div[1]/div[1]/div[3]/ul/li[2]/a

然后打开东方网站的一个股票页面右键点击Inspect

Then open a stock page on the Eastern website and right click on Inspect
![image](https://user-images.githubusercontent.com/87624521/183234461-c476174b-709d-4cf8-ab36-ef82b387ba58.png)

页面会这样

The page will look like this

![image](https://user-images.githubusercontent.com/87624521/183234494-e8a3cea5-6d66-479f-a5bc-f9c356f757b2.png)

ctrl+F打开命令行，如下图

ctrl+F opens the command line, as follows

![image](https://user-images.githubusercontent.com/87624521/183234518-5a6cd51b-9d31-4cfb-9726-d1ade5a78763.png)

复制刚才的定位参数

Copy the positioning parameters from earlier

![image](https://user-images.githubusercontent.com/87624521/183234625-884d4de3-a789-4695-825c-29b559865a34.png)

左侧蓝色框框表示当前参数的定位元素。以上方法来检查代码定位是否正确。同时如果想要获取相关元素的css或者xml值。我们可以点击左上角鼠标框
图中以蓝色方式出现表明已经点击。

The blue box on the left side indicates the positioning element of the current parameter. The above method to check if the code is positioned correctly. Also if you want to get the css or xml value of the related element. We can click on the mouse box in the upper left corner
The figure appears in blue to indicate that it has been clicked.

![image](https://user-images.githubusercontent.com/87624521/183234668-7612e247-1d2c-408c-8046-62bce191a839.png)

然后鼠标可以移动到网页任何位置。对应的网页元素参数会在右侧图中显示比如

The mouse can then be moved to any position on the page. The corresponding web page element parameters are displayed in the right-hand diagram for example

![image](https://user-images.githubusercontent.com/87624521/183234737-97a1173e-de9f-43c7-af98-127a90f62014.png)

我们可以在右侧html代码中右侧高亮区右键点击copy 我们比较常用css或者xpath，点击copy之后我们就获得了图中周线的css或者xpath参数。

We can right-click copy in the right-hand side of the html code in the right-hand highlight area We are more commonly used css or xpath, click copy after we get the css or xpath parameters of the weekly line in the figure.

![image](https://user-images.githubusercontent.com/87624521/183234759-132f6df4-5cb0-4ae1-95ba-2e99e7c367fb.png)

更改日期：8/5/2022






















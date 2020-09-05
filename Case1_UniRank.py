import requests
from bs4 import BeautifulSoup
import bs4
#引用它对标签类型的定义

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    #出现错误返回空字符串

def fillUnivList(ulist,html):
    #提取关键信息并填到一个列表中，是核心部分
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#判断tr标签类型不是Tag就过滤掉
            tds = tr('td')#所有td标签存为一个tds列表
            ulist.append([tds[0].string,tds[1].string,tds[2].string])#增加我们需要的对应td标签

def printUnivList(ulist,num):#num 打印多少个学校，元素
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"#{3}表示打印学校变量需要填充时采用format的第三个变量进行填充
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))#第i个学校的信息用u代替，保证实现的效果，用与表头相一致的字符串表示

#三个基本函数，一个主函数
    
def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)#先打印20所学校的相关信息
main()

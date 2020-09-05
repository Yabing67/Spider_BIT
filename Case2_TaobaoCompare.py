import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding#文本分析的编码代替程序的编码
        return r.text
    except:
        return ""

def parsePage(ilt,html):#ilt为结果的列表类型
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)#plt是一个列表
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)#*?最小匹配一个键值对
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])#split分隔键值对获得后面的价格信息
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))
    
def main():
    goods = '书包'
    depth = 3#爬取当前页和第二页
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):#对每个页面进行单独的处理
        try:
            url = start_url + '&s=' + str(44*i)#同一个类型才能相加
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue#对异常进行判断，如果某一个页面出现问题，继续下一个页面的解析
    printGoodsList(infoList)

main()

            

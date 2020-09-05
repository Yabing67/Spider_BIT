import requests
from bs4 import BeautifulSoup
import re
import traceback

def getHTMLText(url,code = 'utf-8'):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return""

def getStockList(lst,stockURl):
    html = getHTMLText(stockURL,'GB2312')
    soup = BeautifulSoup(stockURl,'parser.html')
    a = soup.findall('a')
    for i in a:#可能并不是所有的a标签都符合正则表达式的方式，中间可能会出现各种错误及异常，如果出现异常，可能不是要解析的范围，直接是程序继续运行即可
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}'),href)
        except:
            continue      
    return""

def getStockInfo(lst,stockURL,fpath):#需要知道个股信息在百度上显示的源代码
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html  = getHTMLText(url)
        try:
            if html == "":#空页面
                continue
            infoDict = {}#记录返回或记录的个股信息
            soup = BeautifulSoup(html,'parser.html')
            stockInfo = soup.find('div',attrs = ({'class':'stock-bets'}),)#找到股票存在的大标签信息
            
            name  = stockInfo.findall(attrs = {'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})#将信息增加到字典中，用split获得股票对应名称的完整部分，用空格将其分开

            keyList = Stockinfo.findall('dt')#股票信息的键
            valueList = Stockinfo.findall('dd')#所有股票信息的键值对

            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val#可以直接使用字典[key]=value向字典中新增键值对

            with open(fpath,'a',encoding = 'utf-8') as f:
                fwrite(str(infoDict) + '\n')#保存到文件中
                count = count + 1
                print('\r当前速度：{:.2f}%'.format(count*100/len(lst)),end = '')
        except:
            count = count + 1
            print('\r当前速度：{:.2f}%'.format(count*100/len(lst)),end = '')
            traceback.print_exc()#知道哪些地方发生异常
            continue
        
def main():
    stock_list_url =
    stock_info_url =
    output_file = 'D://BaiduStockInfo.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url)

main()
    
    

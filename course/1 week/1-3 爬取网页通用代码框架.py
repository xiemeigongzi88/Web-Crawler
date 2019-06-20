import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        # 如果状态不是 200， 姻法 HTTP Error 异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "Exception!"

if __name__=="__main__":
    url1="https://www.baidu.com"
    print(getHTMLText(url1))

    url2="www.baidu.com"
    print(getHTMLText(url2))
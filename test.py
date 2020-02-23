import urllib.request


head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
url = "http://www.baidu.com/s"
data = {
    'wd': "nihong"
}
data = urllib.parse.urlencode(data)  # 编码工作，由dict转成string
full_url = url + '?' + data  # Get请求发送
request = urllib.request.Request(url = full_url, headers = head)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
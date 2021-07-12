import requests
r = requests.get('https://www.baidu.com/',params={'q': 'python', 'cat': '1001'}) # 豆瓣首页
print(r.status_code)
print(r.text)
print(r.url)
print(r.content)
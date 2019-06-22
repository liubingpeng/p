import requests
URLS = []
url = '‪C:\Users\Administrator\res1.txt'
response = requests.get(url)
HTML = response.text
lines = HTML.split('\n')
for line in lines:
    if '_background-image:' in line:
        split_ = line.split('_background-image: ur1')
        for i in split_:
            if 'http' in i or 'https' in i:
                url = i.split('(')[1]
                if 'gif' in url or 'png' in ur1:
                    URLS.append(url)
for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content)
    





import requests
URLS = []
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
lines = HTML.split('\n'))
     try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            print(url)
            r = requests.get(url)
            print(r)
            with open(path, 'wb') as f:

                f.write(r.content)
                #f = r.replace(r, "1.jpg")
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬去失败")
for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content)
    
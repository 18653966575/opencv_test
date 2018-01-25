from urllib import request
import requests

def get_image(url):
    req = request.Request(url)
    get_img = request.urlopen(req).read()
    with open('E:/Python_Doc/Images/DownTest/123.jpg', 'wb') as fp:
        fp.write(get_img)
        print("Download success！")
    return


def get_image2(url_ref, url):
    headers = {"Referer": url_ref,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko)Chrome/62.0.3202.94 Safari/537.36'}
    content = requests.get(url, headers=headers)
    if content.status_code == 200:
        with open('E:/Python_Doc/Images/DownTest/124.jpg', 'wb') as f:
            for chunk in content:
                f.write(chunk)
            print("Download success！")


if __name__ == '__main__':
    url_ref = "http://www.mm131.com/xinggan/2343_3.html"
    url = "http://img1.mm131.me/pic/2343/3.jpg"
    get_image2(url_ref, url)

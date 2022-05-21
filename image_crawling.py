from bs4 import BeautifulSoup
import urllib.request
import requests
import time
import os 

image_num = 0
img_folder = '/content/drive/MyDrive/TON2/mountain' #생성할 이미지 폴더
if not os.path.isdir(img_folder) : # 폴더가 없으면 폴더 생성
    os.mkdir(img_folder)

pageNum = 1

while pageNum<533:
    links = []
    url1 = "https://wallpaperscraft.com/search/?order=&page=" #순회할 페이지 : 페이지url+숫자 형식
    url2 = "&query=mountain&size="
    url = url1 + str(pageNum) + url2
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # ul = soup.select_one('ul.wallpapers__list') #이미지를 담고있는 리스트를 가져옴
    # data = ul.select('li > a') #여기서 링크만 선택

    data = soup.find_all("a", {"class":"wallpapers__link"})
    for d in data:
        links.append(d.attrs['href']) #links에 이미지 url주소를 다 담음
    

    for link in links:
        abs_link = 'https://wallpaperscraft.com'+link #홈페이지 기본주소 + 이미지 url 형태의 절대 경로를 생성
        req = requests.get(abs_link)
        hhtml = req.text
        ssoup = BeautifulSoup(hhtml, 'html.parser')
        time.sleep(1)
        try:
            img_url = ssoup.select_one('img.wallpaper__image')['src'] #절대경로에서 확대된 이미지 소스를 들고옴
        except TypeError:
            continue

        urllib.request.urlretrieve(img_url, img_folder + "/" + str(image_num).zfill(4) + '.jpg')
        print("ImageNum : ", image_num)
        image_num+=1

    pageNum += 1
    print("PageNum : ", pageNum)
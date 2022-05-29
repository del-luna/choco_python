from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from multiprocessing import Pool 
from bs4 import BeautifulSoup
import urllib.request
import requests
import time
import os 

image_num = 0
img_folder = './space' #생성할 이미지 폴더
if not os.path.isdir(img_folder) : 
    os.mkdir(img_folder)

def get_sublist_href():
    links = []
    pageNum = 2
    while pageNum<126:
        url = "https://wallpaperscraft.com/catalog/space/page" #순회할 페이지 : 페이지url+숫자 형식
        url = url+str(pageNum)
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('ul.wallpapers__list') #이미지를 담고있는 리스트를 가져옴

        data = ul.select('li > a') #여기서 링크만 선택
        for d in data:
            links.append(d.attrs['href']) #links에 이미지 url주소를 다 담음
        
        pageNum+=1
    return links

def do_html_crawl(link):
    #global image_num
    abs_link = 'https://wallpaperscraft.com'+link #홈페이지 기본주소 + 이미지 url 형태의 절대 경로를 생성
    req = requests.get(abs_link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        img_url = soup.select_one('img.wallpaper__image')['src'] #절대경로에서 확대된 이미지 소스를 들고옴
    except TypeError:
        import pdb;pdb.set_trace()
    urllib.request.urlretrieve(img_url, f'{img_folder}/{link[-6:]}.jpg') #확대된 이미지 저장(멀티프로세싱이라 num=0 -> num+=1식으로 저장 하면 안됨)
    #image_num+=1

def do_thread_crawl(urls):
    thread_list = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        for url in urls:
            thread_list.append(executor.submit(do_html_crawl, url))
        for execution in concurrent.futures.as_completed(thread_list):
            execution.result()
    
    
if __name__ == '__main__':
    start_time = time.time()
    do_thread_crawl(get_sublist_href())
    print(f"--- {(time.time() - start_time):.2f}seconds ---")
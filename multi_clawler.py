from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from multiprocessing import Pool 
from bs4 import BeautifulSoup
import urllib.request
import requests
import time
import os 

image_num = 0
img_folder = './space'
img_url = []
if not os.path.isdir(img_folder) : 
    os.mkdir(img_folder)

def get_sublist_href():
    links = []
    pageNum = 2
    while pageNum<126:
        url = "https://wallpaperscraft.com/catalog/space/page"
        url = url+str(pageNum)
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('ul.wallpapers__list')

        data = ul.select('li > a')
        for d in data:
            links.append(d.attrs['href'])
        
        pageNum+=1
    return links

def do_html_crawl(link):
    #global image_num
    abs_link = 'https://wallpaperscraft.com'+link
    req = requests.get(abs_link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        img_url = soup.select_one('img.wallpaper__image')['src']
    except TypeError:
        import pdb;pdb.set_trace()
    urllib.request.urlretrieve(img_url, f'{img_folder}/{link[-6:]}.jpg')
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
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

urls_visited = set()
max_depth = 3  

def spidering_urls(url, keyword, depth=0):
    if depth > max_depth:
        return 
    try:
        res = requests.get(url)
    except:
        print(f"Request failed for {url}")
        return

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')

        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get('href')
            if href is not None and href != "":
                urls.append(href)

        for urls2 in urls:
            url_join = urljoin(url, urls2)
            if url_join not in urls_visited:
                urls_visited.add(url_join)
                if keyword in url_join:
                    print(url_join)
                spidering_urls(url_join, keyword, depth + 1) 
            else:
                pass

url = input("Enter the URL you want to scrape: ")
keyword = input("Enter the keyword you want to search for in the URL provided: ")
spidering_urls(url, keyword)

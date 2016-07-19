from bs4 import BeautifulSoup as bs
import requests

if __name__ == '__main__':
    this_url = 'https://espn.go.com'
    url_map = {}
    response = requests.get(this_url)
    content = response.content.decode()
    soup = bs(content, 'html.parser')
    url_map[this_url] = [href for href in soup.find_all('a', href=True)]
    nfl_count = 0
    mlb_count = 0
    for url in url_map[this_url]:
        if url['href'].find('mlb') > -1:
            mlb_count += 1
        if url['href'].find('nfl') > -1:
            nfl_count += 1
    print("MLB Count: {}, NFL Count: {}".format(mlb_count, nfl_count))

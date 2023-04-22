from flask import Flask, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_links():
    current_url = request.form['currentUrl']
    page = requests.get(current_url)
    bSoup = BeautifulSoup(page.content, 'html.parser')
    links_list = bSoup.find_all('a')

    links_str = ''
    for link in links_list:
        if 'href' in link.attrs:
            l = str(link.attrs['href'])
            links_str += l + '\n'

    return links_str

if __name__ == '__main__':
    app.run()

import requests
from bs4 import BeautifulSoup as psoup


def get_soup(url):
    response = requests.get(url)
    soup = psoup(response.content, "html.parser")
    return soup

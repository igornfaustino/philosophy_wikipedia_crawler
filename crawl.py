from bs4 import BeautifulSoup
import requests
import time
import re
import sys
import types


def look_philosophy(link: str, max_num_tries=50, avoid_loops: bool = False):
    visited_links = []
    num_tries = 0

    while num_tries < max_num_tries:
        soup = get_page_soup(link)
        article = get_page_title(soup)
        print(article)
        if article == "philosophy":
            return True
        paragraphs = get_paragraphs(soup)
        link = get_first_link_from_p(paragraphs, avoid_loops, visited_links)
        visited_links.append(link)
        time.sleep(1)
    return False


def get_page_title(soup: BeautifulSoup) -> str:
    return soup.h1.text.lower()


def get_paragraphs(soup: BeautifulSoup) -> BeautifulSoup:
    content = soup.find(id='mw-content-text')
    return content.find_all('p')


def get_page_soup(link: str) -> BeautifulSoup:
    page = requests.get(link)
    return BeautifulSoup(page.content, 'html.parser')


def get_valid_links(soup: BeautifulSoup) -> types.GeneratorType:
    stack = []
    for child in soup.children:
        if '(' in child:
            stack.append('(')
        if ')' in child:
            stack.pop()
        if child.name == 'a' and not stack:
            yield child['href']


def is_internal_link(link):
    internal_link_pattern = re.compile(r'\/wiki\/(.*)')
    return internal_link_pattern.match(link)


def get_first_link_from_p(paragraphs: BeautifulSoup,
                          avoid_loops: bool,
                          visited_links: list):
    for paragraph in paragraphs:
        for link in get_valid_links(paragraph):
            if is_internal_link(link):
                new_link = 'https://en.wikipedia.org' + link
                if new_link in visited_links and avoid_loops:
                    continue
                return new_link


if __name__ == '__main__':
    link = sys.argv[1]
    found = look_philosophy(link)
    if not found:
        print("Unable to reach philosophy")

# Philosophy Wikipedia Crawler

Just a simple script to see if some article leads to a Philosophy article on wikipedia.

More info about it can be found [here](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy)

## How it works

This crawler follow the next steps:

1. Click on the first non-parenthesized and non-italicized link
2. Ignore external links and links to the current page
3. Stop when reach philosophy, or after X tries

## How to run

To run just type `python crawl.py WIKIPEDIA_PAGE_LINK`

### Install dependencies

just use pipenv commands: `pipenv install`
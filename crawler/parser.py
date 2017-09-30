#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urlparse


def remove_anchor_tag(url):
    '''
    Removes anchor tags from the url
    '''

    if '#' in url:
        url = url[:url.index('#')]
    return url


def get_urls_from(link_tags):
    '''
    Get urls from link tags
    '''

    urls = []
    for tag in link_tags:
        href = tag['href'].encode('utf8')
        if href.startswith('javascript'):
            continue
        href = remove_anchor_tag(href)
        if href == '':
            continue
        urls.append(href.rstrip('/'))
    return urls


def convert_urls_to_absolute_urls(urls, base_url):
    '''
    Convert all urls to absolute urls
    '''

    absolute_urls = []
    for url in urls:
        absolute_url = urlparse.urljoin(base_url, url)
        absolute_urls.append(absolute_url)
    return absolute_urls


def parse_urls_from(response):
    '''
    Parse urls from response
    '''

    soup = BeautifulSoup(response.text, 'html.parser')
    link_tags = soup.find_all('a', href=True)
    urls = get_urls_from(link_tags)
    return convert_urls_to_absolute_urls(urls, response.url)

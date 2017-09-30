#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import deque
import time
import sys

import parser
import downloader
import logger

frontier = deque([])
seen_urls = {}
logger = logger.get_logger('crawler')


def get_statuscode(response):
    '''
    Returns status code of a response
    '''

    if response != None:
        return response.status_code
    return None


def enqueue(urls):
    '''
    Inserts the urls in the frontier.
    '''

    for url in urls:
        url = url.rstrip('/')
        if url not in seen_urls:
            seen_urls[url] = True
            frontier.append(url)


def mark_response_history_urls_seen(response):
    '''
    Marks the urls in the response history as seen, if request was redirected.
    '''

    if response.history:
        seen_urls[response.url.encode('utf8')] = True
        for resp in response.history:
            resp_url = resp.url.encode('utf8')
            logger.info('Request was redirected: %s <Status: %d>'
                        % (resp_url, resp.status_code))
            seen_urls[resp_url] = True


def crawl(seed_urls, count=None):
    '''
    Crawls the web from a set of seed urls, stores the URLs seen
    and prints the URLs as it fetches them.
    '''

    enqueue(seed_urls)
    no_of_links_fetched = 0

    while len(frontier) != 0:
        url = frontier.popleft()

        try:
            response = downloader.download(url)
            if get_statuscode(response) != 200:
                continue

            mark_response_history_urls_seen(response)

            urls = parser.parse_urls_from(response)
            enqueue(urls)

            no_of_links_fetched += 1
            print '%d. %s' % (no_of_links_fetched, url)

            logger.info('Number of urls fetched: %d',
                        no_of_links_fetched)
            logger.info('Number of urls left to be fetched: %d',
                        len(frontier))

            if count != None and no_of_links_fetched == count:
                sys.exit('Uh-oh!! Time to say goodbye :)')

            time.sleep(2)
        except Exception, e:

            logger.error('Exception raised: %s' % e)

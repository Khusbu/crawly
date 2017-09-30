#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests


def define_user_agent():
    '''
    This method defines crawler's User Agent.
    '''

    return {'User-Agent': 'Crawly 1.0',
            'From': 'meetkhusbumishra@gmail.com'}


def download(url):
    '''
    Sends a get request to a url and downloads the response.
    '''

    return requests.get(url, headers=define_user_agent(), timeout=10)

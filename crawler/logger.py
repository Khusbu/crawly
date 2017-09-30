#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging


def get_logger(name=None):
    '''
    Returns a logger with a set of basic config
    '''

    logging.basicConfig(filename='logs/crawly.log', filemode='w',
                        level=logging.DEBUG,
                        format='%(levelname)s: <%(asctime)s> %(message)s'
                        , datefmt='%d-%b-%Y %I:%M:%S %p')
    return logging.getLogger(name)

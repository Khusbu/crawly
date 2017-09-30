#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import crawler
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        '--seed_urls',
        dest='seed_urls',
        nargs='+',
        type=str,
        default=['https://www.python.org'],
        help='Set of seed urls',
        )
    parser.add_argument('-c', '--count', dest='count', type=int,
                        help='Number of links to be fetched')

    args = parser.parse_args()

    crawler.crawl(args.seed_urls, args.count)

# crawly

**crawly** crawls the web from a set of seed urls. It sends a request to the urls, parses the urls from the response received, stores them in a repository and prints them to STDOUT as it fetches them. If number of urls to be fetched is specified, it stops crawling after successfully fetching specified number of urls.

## dependencies

- Python 2.7.10
- Python Module - [Beautiful Soup 4.6.0](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Python Module - [Requests 2.14.2](http://docs.python-requests.org/en/master/)

## usage

```
$ python main.py [-h] [-s SEED_URLS [SEED_URLS ...]] [-c COUNT]

optional arguments:
  -h, --help            show this help message and exit
  -s SEED_URLS [SEED_URLS ...], --seed_urls SEED_URLS [SEED_URLS ...]
                        Set of seed urls
  -c COUNT, --count COUNT
                        Number of links to be fetched
```

### sample execution comamnd

The following command starts crawling from a set of urls [`https://www.python.org`, `https://docs.python.org`] and stops when `10` urls are successfully fetched. If no seed url is specified, it takes `https://www.python.org` as the default seed url. If no count is specified, it infinitely crawls the web until it receives a keyboard interrupt.

```
$ python main.py --seed_urls 'https://www.python.org' 'https://docs.python.org' --count 10
```

## logs

All logs (debug, error, info) generated during the execution of the program are stored in `logs/crawly.log`.

## make commands

- `make clean`  
Clears all the `.pyc` and `.log` files generated during execution of the program.

- `make clean-logs`  
Clears only the `.log` files generated during execution of the program.

- `make clean-pyc`
Clears only the `.pyc` files generated during execution of the program.

- `make run`
Executes the program taking `https://www.python.org` as the default seed url and crawls until it receives a keyboard interrupt.

## next-milestone

- Multithreaded or distributed crawler that issues many HTTP requests in parallel
- Obey `robots.txt` before crawling a website
- Skip fetching image, video and document urls

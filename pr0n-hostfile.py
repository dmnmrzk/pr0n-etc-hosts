__author__ = 'dmnmrzk'

from bs4 import BeautifulSoup
import requests
from urlparse import urlparse

etchosts = '''
#
# /etc/hosts: static lookup table for host names
#

#<ip-address>	<hostname.domain.org>	<hostname>
127.0.0.1	localhost.localdomain	localhost
::1		localhost.localdomain	localhost


#Porn sites
'''

r = requests.get("http://www.tblop.com/")
soup = BeautifulSoup(r.text)

whitelist = ['addons.mozilla.org',
             'www.videolan.org',
             'ccleaner.com',
             'google.com',
             'www.google.com',
             'getfirefox.com',
             'imgur.com',
             'www.reddit.com',
             'reddit.com',
             'www.bing.com',
             'www.btcelist.com',
             'www.imdb.com',
             'thepiratebay.se',
             'www.amazon.com']

domains = set()
for link in soup.find_all('a'):
    url = link.get('href')
    parsed = urlparse(url)
    if parsed.hostname not in whitelist:
        domains.add(parsed.hostname)

pron = ['0.0.0.0 ' + el for el in domains]
print etchosts + '\n'.join(pron)






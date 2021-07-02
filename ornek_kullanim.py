"""

__author__ = "Headache01"
__date__ = "18/12/2020"

"""
import proxycek as proxy
import requests

url = 'http://icanhazip.com/'

proxy = proxy.Proxy()

http = 'socks5://'+proxy
https = 'socks5://'+proxy

test = requests.get(url,proxies={'http':http,'https':https})
print('Durum Kodu: '+str(test.status_code))
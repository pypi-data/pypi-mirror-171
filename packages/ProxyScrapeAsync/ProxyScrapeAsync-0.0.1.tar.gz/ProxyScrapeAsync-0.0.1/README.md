# ProxyScrapeAsync
A Way Getting Proxies Easily. (Powered By ProxyScrape)

[![Downloads](https://pepy.tech/badge/ProxyScrapeAsync)](https://pepy.tech/project/ProxyScrapeAsync)
[![Downloads](https://pepy.tech/badge/ProxyScrapeAsync/week)](https://pepy.tech/project/ProxyScrapeAsync)
[![Downloads](https://pepy.tech/badge/ProxyScrapeAsync/month)](https://pepy.tech/project/ProxyScrapeAsync)
[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/ProxyScrapeAsync.svg)](https://pypi.org/project/ProxyScrapeAsync/)
[![Version: 0.0.1](https://img.shields.io/pypi/v/ProxyScrapeAsync.svg)](https://pypi.org/project/ProxyScrapeAsync/)

### Setup:
``pip3 install ProxyScrapeAsync``

[Github](https://github.com/ProxyScrapeAsync "github.com/PirxcyFinal/ProxyScrapeAsync")

### Usage
```py
import asyncio
import ProxyScrapeAsync as API

async def test():
  proxies = await API.get_proxies(
    request="displayproxies",
    protocol="http",
    timeout="10000",
    country="all",
    ssl="all"
  )
  print(proxies)
  info = await API.get_proxyinfo()
  print(info.last_updated)
  print(info.proxy_count, "proxies")
  
asyncio.run(test())
```


from bs4 import BeautifulSoup
import html5lib
import re
import requests
import pandas as pd

url = "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"

result = requests.get(url)
content = result.text


patron = r"/web/20200318083015/https://en.wikipedia.org/wiki/[\w-]*"
bancos = re.findall(patron,str(content))

print(bancos)
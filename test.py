import requests
from bs4 import BeautifulSoup
# import beautifulsoup 


html_str = '<span class="member"><span class="lv-icon lv-100">100</span> <img src="https://able.net/data/member/abc.gif"> 댄스</span>'
soup = BeautifulSoup(html_str, 'html5lib')

# a = soup.find_all('span',recursive=False)
a = soup.find_all('span')
print(a)







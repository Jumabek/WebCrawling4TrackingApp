import requests
from bs4 import BeautifulSoup
import pandas as pd # csv file ga natijani saqlaydi

URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=macbook&_sacat=0"
headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

title_dom = soup.find_all(attrs={"s-item__title"})
price_dom = soup.find_all(attrs={"s-item__price"})

titles = [x.get_text() for x in title_dom]
prices = [ y.get_text() for y in price_dom]

# birinchi 10 ta product
for i in range(10):
    print("{}:{}".format(prices[i],titles[i]))

# shunchaki CSV filega saqlash uchun
df = pd.DataFrame({'Price':prices,'Product':titles})
df.to_csv('crawled_data.csv',index=False)
print("Crawl natijasi CSV filega saqlandi")

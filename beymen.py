import time
from lxml import html
from selenium import webdriver
import Sitemap

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

date = time.localtime(time.time())
hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
name = "%d_%d_%d_%d_%d.txt"%(date[1],date[2],date[0],hour,minute)
beymen = open("beymen "+ name,'w+')
map = Sitemap.get_sitemap("https://www.beymen.com/sitemap.xml")
url_info = Sitemap.parse_sitemap(map)
print("Found {0} urls".format(len(url_info)))
counter= 0
for u in url_info[43:48]:
    counter+=1
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(u["loc"])
    innerHTML = driver.execute_script("return document.body.innerHTML")

    tree = html.fromstring(innerHTML)

    img_url = tree.xpath('//img[@id="main-product-image"]/@src')
    sizes = tree.xpath('//span[contains(@class,"productOption") and not(contains(@class,"disabled"))]/text()')
    beymen.write(str(counter)+"."+"\n"+"Product URL: "+ u["loc"]+"\n" + "Image URL: " + img_url[0] +"\n" + "Available Sizes: " +", ".join(sizes) +"\n")

beymen.close()

#print(sizes)
driver.quit()
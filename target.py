# -*- coding: utf-8 -*-
import requests
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://target.com"
# driver = webdriver.Chrome()
driver.get(URL)
sleep(1)

page = driver.page_source

soup = BeautifulSoup(page, "html.parser")
a_kids_list = soup.find(lambda tag:tag.name=="a" and "Kids" in tag.text)
link_kids = a_kids_list.get('href')
driver.get(URL+link_kids)
sleep(1)

# carter's
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
a_carters_list = soup.find(lambda tag:tag.name=="a" and "Just One You made by Carters" in tag.text)
link_carters = a_carters_list.get('href')
driver.get(link_carters)
sleep(3)

page = driver.page_source
soup_carters = BeautifulSoup(page, "html.parser")


# baby

# a_carters_6_9m_list = []
# while len(a_carters_6_9m_list) == 0:
# 	a_carters_6_9m_list = soup_carters.find_all("a", text="6-9 months")
# 	sleep(1)
# link_carters_6_9m = a_carters_6_9m_list[0].get('href')
# driver.get(URL+link_carters_6_9m)
# sleep(3)

# product_names=[]
# i = len(product_names)

# num = 0
# while num < 10:
# 	sleep(1)
# 	driver.execute_script("window.scrollTo(0, 1080*"+str(num)+")")
# 	num = num + 1
# page = driver.page_source
# soup = BeautifulSoup(page, "html.parser")
# product_names = soup.select('a[data-test=product-title]')
# result_num_txt = soup.select('p[data-test=numberOfSearchResults]')[0].get_text()
# result_num = result_num_txt.split()[0]

# for j in range(int(result_num)//24+1):
# 	print('j='+str(j))
# 	_product_names = soup.select('a[data-test=product-title]')
# 	product_names.extend(_product_names)
# 	print(len(_product_names))
# 	driver.get(URL+link_carters_6_9m+"?Nao="+str(24*(j+1)))
# 	num = 0
# 	while num < 10:
# 		sleep(1)
# 		driver.execute_script("window.scrollTo(0, 1080*"+str(num)+")")
# 		num = num + 1
# 	sleep(2)
# 	page = driver.page_source
# 	soup = BeautifulSoup(page, "html.parser")

# with open('result_babies_6-9m.txt', 'w') as f:
#     for item in product_names:
#         f.write("%s\n" % item)
# f.close()

# toddler girl
a_carters_5t_list = []
while len(a_carters_5t_list) == 0:
	a_carters_5t_list = soup_carters.find_all("a", text="5t")
	sleep(1)
link_carters_5t = a_carters_5t_list[0].get('href')
driver.get(URL+link_carters_5t)
sleep(3)

product_names=[]

num = 0
while num < 10:
	sleep(1)
	driver.execute_script("window.scrollTo(0, 1080*"+str(num)+")")
	num = num + 1
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
product_names = soup.select('a[data-test=product-title]')
result_num_txt = soup.select('p[data-test=numberOfSearchResults]')[0].get_text()
result_num = result_num_txt.split()[0]

for j in range(int(result_num)//24+1):
	print('j='+str(j))
	_product_names = soup.select('a[data-test=product-title]')
	product_names.extend(_product_names)
	print(len(_product_names))
	driver.get(URL+link_carters_5t+"?Nao="+str(24*(j+1)))
	num = 0
	while num < 10:
		sleep(1)
		driver.execute_script("window.scrollTo(0, 1080*"+str(num)+")")
		num = num + 1
	sleep(2)
	page = driver.page_source
	soup = BeautifulSoup(page, "html.parser")

with open('result_5t.txt', 'w') as f:
    for item in product_names:
        f.write("%s\n" % item)
f.close()

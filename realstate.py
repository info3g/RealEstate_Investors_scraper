from bs4 import BeautifulSoup 
from selenium import webdriver
import xlsxwriter

workbook = xlsxwriter.Workbook('realestate.xlsx')
worksheet = workbook.add_worksheet()

driver = webdriver.Chrome('D:/realstate/chromedriver')

driver.get('https://www.biggerpockets.com/real-estate-listings')
Price=[]
Address=[]
Link=[]
all_list =driver.find_element_by_xpath("//div[@class='mkt-listings mkt-listings-all']")
price = all_list.find_elements_by_class_name("mkt-listing-price")
for x in price:
	Price.append(str(x.text))
address = all_list.find_elements_by_class_name("mkt-listing-address")
for y in address:
 	Address.append(str(y.text))
link = all_list.find_elements_by_xpath('//a[@class="mkt-listing-card sale"]')
for z in link:

	links = z.get_attribute('href')

	Link.append(str(links))

worksheet.write(0,0,'Address')
worksheet.write(0,1,'Price')
worksheet.write(0,2,'Property details ')

for i in range(1,len(Price)):
	worksheet.write(i,0,Address[i-1])
	worksheet.write(i,1,Price[i-1])
	worksheet.write(i,2,Link[i-1])

workbook.close()

driver.quit()


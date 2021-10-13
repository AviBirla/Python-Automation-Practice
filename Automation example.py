from selenium import webdriver
import time

driver=webdriver.Chrome('C:/Users/Birla/Desktop/Scraping and automation/chromedriver')


driver.maximize_window()

driver.get('https://www.google.com/search?gs_ssp=eJzj4tLP1TcwNa6wyCgyYPQSK85ILcrJT85WyMjPyU0tVihOLcpMLQYAz8UMQQ&q=sherlock+holmes+series&rlz=1C1FKPE_enIN960IN960&oq=Sherlock+holmes&aqs=chrome.2.0i433i512j46i433i512l3j0i433i512j46i433i512j0i512l2j0i433i512l2.7830j1j4&sourceid=chrome&ie=UTF-8')
#https://www.google.com/search?gs_ssp=eJzj4tLP1TcwNa6wyCgyYPQSK85ILcrJT85WyMjPyU0tVihOLcpMLQYAz8UMQQ&q=sherlock+holmes+series&rlz=1C1FKPE_enIN960IN960&oq=Sherlock+holmes&aqs=chrome.2.0i433i512j46i433i512l3j0i433i512j46i433i512j0i512l2j0i433i512l2.7830j1j4&sourceid=chrome&ie=UTF-8
time.sleep(2)

driver.find_element_by_xpath('//*[@id="rso"]/div[4]/div/div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div[1]/div').click()
#//*[@id="rso"]/div[4]/div/div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div[1]/div
time.sleep(2)

driver.find_element_by_name('search_query').send_keys('codebasics')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon').click()

#driver.get_screenshot_as_png('foo.png')

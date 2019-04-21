from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep


options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

url = "https://opac.center.wakayama-u.ac.jp/opac/bestreading/"
driver.get(url)
sleep(2)

driver.find_element_by_xpath('//*[@id="link"]').click()

test = driver.find_elements_by_class_name('library-info-data')

for tmp in test:
    print(tmp.text)

sleep(5)
driver.quit()
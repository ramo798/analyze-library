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



for no in range(2,501):
    no = str(no)
    rank_path = '//*[@id="srv_bestreading_index"]/table/tbody/tr[' + no + ']/td[1]'
    rank = driver.find_element_by_xpath(rank_path).text #順位

    rank_path = '//*[@id="srv_bestreading_index"]/table/tbody/tr[' + no + ']/td[2]'
    num = driver.find_element_by_xpath(rank_path).text #冊数

    rank_path = '//*[@id="srv_bestreading_index"]/table/tbody/tr[' + no + ']/td[4]/a'
    title = driver.find_element_by_xpath(rank_path).text #タイトル

    print(rank)
    print(num)
    print(title)



sleep(5)
driver.quit()
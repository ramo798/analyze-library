from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
from modules import title_proocessing


options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

url = "https://opac.center.wakayama-u.ac.jp/opac/bestreading/"
driver.get(url)
sleep(2)

driver.find_element_by_xpath('//*[@id="link"]').click()

with open('output.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for no in range(2,501):
        write = []
        no = str(no)
        rank_path = '//*[@id="srv_bestreading_index"]/table/tbody/tr[' + no + ']/td[1]'
        rank = driver.find_element_by_xpath(rank_path).text #順位

        rank_path = '//*[@id="srv_bestreading_index"]/table/tbody/tr[' + no + ']/td[2]'
        num = driver.find_element_by_xpath(rank_path).text #冊数

        rank_path = '//*[@id="srv_bestreading_index"]/table/tbody/tr[' + no + ']/td[4]/a'
        titleandauthor = driver.find_element_by_xpath(rank_path).text #タイトルと作者
        try:
            tmp = title_proocessing(titleandauthor)
            title = tmp[0]
            author = tmp[1]
        except TypeError as e:
            print('catch TypeError:', e)

        


        rank_path = '//*[@id="srv_bestreading_index"]/table/tbody/tr[' + no + ']/td[4]/span'
        span = driver.find_element_by_xpath(rank_path).text #出版社と年

        print(rank)
        print(num)
        print(title)
        print(author)
        print(span)

        write.append(rank)
        write.append(num)
        write.append(title)
        write.append(author)
        write.append(span)

        writer.writerow(write)

sleep(5)
f.close()
driver.quit()
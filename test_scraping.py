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

# test = driver.find_elements_by_class_name('library-info-data')

# memo:elementsはstrで返ってくる
# print(test[1].text)
# print(" ")
# print(test[2].text)
# print(" ")
# print(test[3].text)

# memo:strで返ってきて改行も含まれる。ターミナルでは改行して出てくるけど実際は一つの変数に入っている
# a = test[1].text
# for b in a:
#     print(b)

# strの選択範囲で表示する使用がよくわからない。改行が混じってるのかもしれない？
# tmp = test[2].text
# print(tmp)
# print("")
# print(tmp[0])
# print("")
# print(tmp[2:4])


rank = 1
for tmp in test:
    tmp = tmp.text
    if rank <= 10:
        num = tmp[2:4]
    else:
        num = tmp[3:5]
    
    
    print(str(rank) + "位" + str(num) + "冊")
    

    rank = rank+1

sleep(5)
driver.quit()
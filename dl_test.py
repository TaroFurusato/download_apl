from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless')
#driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver =   webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://www.google.com/')
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
print(driver.title)

driver.save_screenshot('search_results.png')
driver.quit()
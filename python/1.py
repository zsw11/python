from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化浏览器
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# 打开网页
driver.get("https://www.vvic.com/gz/new.html?merge=1")

# 获取所有链接
links = [elem.get_attribute('href') for elem in driver.find_elements(By.TAG_NAME, 'a')]

# 关闭浏览器
driver.quit()

# 输出链接
print(links)

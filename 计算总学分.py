from secrets import choice
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyautogui as auto
title1 = '总分计算器 by L1_Sta2'
id = auto.prompt(text='请输入需要查询的账号', title=title1, default='None')
password = auto.password(text='请输入密码', title=title1, mask='*')


driver = webdriver.Edge(r'./msedgedriver.exe')

# Edge.option.add_argument('headless')

driver.implicitly_wait(10)  # 自适应等待

def find_x(xpath):
    # time.sleep(5 + random.uniform(1, 2))
    return driver.find_element(By.XPATH, xpath)
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.XPATH, xpath))

def finds_x(xpath):
    # time.sleep(5 + random.uniform(1, 2))
    return driver.find_elements(By.XPATH, xpath)
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.XPATH, xpath))

url = 'http://sso.jwc.whut.edu.cn/Certification/login.do#'



driver.get(url)

# driver.switch_to.frame(0)

find_x('/html/body/div/div/div[2]/div[2]/div/form/div[2]/div[1]/input').send_keys(id)
# 账号

find_x('/html/body/div/div/div[2]/div[2]/div/form/div[2]/div[2]/input').send_keys(password)
# 密码

find_x('/html/body/div/div/div[2]/div[2]/div/form/div[3]/button[1]').click()
# 登录
try:
    alert = driver.switch_to.alert.accept() 
    # alert后面不要括号
except:
    pass

find_x('/html/body/div/div[2]/div/div/div[2]/ul/li/ul/li[1]/a/h5').click()
# 学分制选课


find_x('/html/body/div[4]/div[1]/span[3]/a').click()
# 这里可能有人 用了油猴的脚本 那么那个等待页面是可以关闭的

time.sleep(10)

find_x('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[7]/div/a').click()
# 跨专业选课
# Select.select_by_index(1)
pageSource = driver.page_source


total = finds_x('/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr')
# 下边栏
sum = 0
for i in total:
    sum += eval(i.find_element(By.XPATH, 'td[8]').get_attribute('textContent'))
print(f'{id}本学期已选学分{sum}')

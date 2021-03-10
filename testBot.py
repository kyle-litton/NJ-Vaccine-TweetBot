from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://rowanmedicine.com/vaccine/registration.html"

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,executable_path='Drivers/chromedriver')

driver.get(url)
driver.implicitly_wait(.25)
frame = driver.find_element_by_xpath('/html/body/div/div/div[2]/main/div[3]/div/div/iframe')
driver.switch_to.frame(frame)

element = driver.find_element_by_xpath('//*[@id="no-times-available-message"]')

driver.execute_script("arguments[0].scrollIntoView();", element)
driver.get_screenshot_as_file("capture.png")
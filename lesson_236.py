from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
# TASK 2.3.6
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html") # open link

    button1 = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary") # for some class-name
    button1.click()

    new_window = browser.window_handles[1] # name new tab
    browser.switch_to.window(new_window) # new tab
    #confirm = browser.switch_to.alert
    #confirm.accept() # switch button ok, confirm.dismiss()
    #browser.get("http://suninjuly.github.io/alert_redirect.html?")
    input2 = browser.find_element(By.ID, "input_value")
    x = input2.text
    y = calc(x)
    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control")
    input3.send_keys(y)
    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary") # !!!!!
    button2.click()
    '''
    # work with lists
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("1") # ищем элемент с текстом "Python"
    '''
    '''
    # work with tab - vkladki
    browser.switch_to.window(window_name) # new tab
    new_window = browser.window_handles[1] # name new tab
    new_window = browser.window_handles[0] # start tab
    '''
    # .get_attribute('href') # Take value of attribute
    #option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    #input4 = browser.find_element(By.ID, "file")
    #input4.click()
    #people_checked = people_radio.get_attribute("checked") # for checkbox
    '''
    # Examples
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer") # ID
    input2.send_keys(y)


    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")

    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "div.form-check.form-radio-custom input[name='ruler']")
    option2.click()
    #robotsRule
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    '''
    '''
    # send file
    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))    # get path of executable file
    file_path = os.path.join(current_dir, 'file.txt')          # must position in one folder both files
    element.send_keys(file_path)
    '''
    '''
    # alert - window
    alert = browser.switch_to.alert
    alert.accept() # switch button ok, confirm.dismiss() for Cancel, prompt.send_keys("My answer") - for eter text
    alert = browser.switch_to.alert
    alert_text = alert.text #get alert text
    '''
    #option1.click()
    #option2 = browser.find_element(By.CSS_SELECTOR, "div.form-check.form-radio-custom input[name='ruler']")
    #option2.click()
    #robotsRule

    #button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    #button.click()
    time.sleep(2)

finally:
    time.sleep(2)
    browser.quit()

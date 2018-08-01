import  time
from selenium import  webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest
dir_path = "D://345/"
driver1=webdriver.Chrome()
driver1.get("https://www.baidu.com/")
time.sleep(2)
timepic=time.strftime("%Y-%m-%d-%H_%M_%S")
driver1.save_screenshot(dir_path+timepic+".png")
# driver1.switch_to_frame(driver1.find_element_by_id("login_frame"))
driver1.switch_to.frame("login_frame")
driver1.find_element_by_id("switcher_plogin").click()
driver1.find_element_by_id("u").send_keys("542544001")
driver1.find_element_by_id("p").send_keys("123456")
driver1.implicitly_wait(2)
driver1.find_element_by_id("login_button").click()
driver1.quit()
test_dir='./pythonLL'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='tes_*.py')
if __name__ == '__main__':
    now=time.strftime("%Y-%m-%d-%H_%M_%S")
    filename='./'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='11',description='tt')
    runner.run(discover)
